import uuid
from decimal import Decimal
from django.db import models

from user.models import Profile, serviceProviders
from post.models import Service, Path

class Bank(models.Model):
    bank_name = models.CharField(max_length=100)
    account_number = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.bank_name} - Account Number: {self.account_number}"

class Order(models.Model):
    STATUS_CHOICES = (
        ('on_progress', 'On Progress'),
        ('completed', 'Completed'),
    )

    consumer = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, related_name='my_orders')
    service = models.ForeignKey(Service, on_delete=models.SET_NULL, null=True, related_name='orders')
    path = models.ManyToManyField(Path, related_name='order_path')
    created_at = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    approved = models.BooleanField(default=False)
    payment_completed = models.BooleanField(default=False)
    order_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    bank = models.ForeignKey(Bank, on_delete=models.SET_NULL, null=True, related_name='orders')
    final_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='on_progress')

    def __str__(self):
        return f"Order ID: {self.order_id} - Consumer: {self.consumer} - Service: {self.service}"

    def save(self, *args, **kwargs):
        if self.total_price:
            self.final_price = self.total_price - (Decimal(0.1) * self.total_price)
        super().save(*args, **kwargs)

    def update(self, *args, **kwargs):
        if self.total_price:
            self.final_price = self.total_price - (Decimal(0.1) * self.total_price)
        super().update(*args, **kwargs)


class PaymentInvoice(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE, related_name='payment_invoice')
    payment_date = models.DateTimeField(auto_now_add=True)
    transaction_id = models.CharField(max_length=100, blank=True)
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return f"Invoice for Order ID: {self.order.order_id} - Payment Date: {self.payment_date}"
    

class ApproveDelivery(models.Model):
    order = models.OneToOneField(Order, on_delete=models.SET_NULL, null=True, related_name='approved_delivery')
    provider_approve = models.BooleanField(default=False)
    consumer_approve = models.BooleanField(default=False)
    paid = models.BooleanField(default=False)

    def __str__(self):
        return f"ApproveDelivery for Order ID: {self.order.order_id}"
    

class Rating(models.Model):
    provider = models.ForeignKey(serviceProviders, on_delete=models.CASCADE, related_name='ratings', null=True)
    consumer = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='ratings', null=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='ratings')
    rating = models.PositiveIntegerField()
    description = models.TextField(blank=True)
