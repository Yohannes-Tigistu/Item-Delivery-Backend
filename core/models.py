import uuid
from django.db import models

from user.models import Profile
from post.models import Service, Path

class Bank(models.Model):
    bank_name = models.CharField(max_length=100)
    account_number = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.bank_name} - Account Number: {self.account_number}"

class Order(models.Model):
    consumer = models.ForeignKey(Profile, on_delete=models.DO_NOTHING, related_name='my_orders')
    service = models.ForeignKey(Service, on_delete=models.DO_NOTHING, related_name='orders')
    path = models.ManyToManyField(Path, related_name='order_path')
    created_at = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    approved = models.BooleanField(default=False)
    payment_completed = models.BooleanField(default=False)
    order_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    bank = models.ForeignKey(Bank, on_delete=models.SET_NULL, null=True, related_name='orders')

    def __str__(self):
        return f"Order ID: {self.order_id} - Consumer: {self.consumer} - Service: {self.service}"
    

class PaymentInvoice(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE, related_name='payment_invoice')
    payment_date = models.DateTimeField(auto_now_add=True)
    transaction_id = models.CharField(max_length=100, blank=True)
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return f"Invoice for Order ID: {self.order.order_id} - Payment Date: {self.payment_date}"