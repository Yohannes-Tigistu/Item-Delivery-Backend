from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Order, PaymentInvoice

@receiver(pre_save, sender=Order)
def update_invoice(sender, instance, **kwargs):
    if instance.pk:
        try:
            old_instance = Order.objects.get(pk=instance.pk)
        except Order.DoesNotExist:
            return
        
        if old_instance.approved != instance.approved:
            if instance.approved:
                PaymentInvoice.objects.create(order=instance)
            else:
                PaymentInvoice.objects.filter(order=instance).delete()


@receiver(pre_save, sender=PaymentInvoice)
def update_order_payment_completed(sender, instance, **kwargs):
    if instance.pk:
        try:
            old_instance = PaymentInvoice.objects.get(pk=instance.pk)
        except PaymentInvoice.DoesNotExist:
            return
        
        if not old_instance.is_paid and instance.is_paid:
            order = instance.order
            order.payment_completed = True
            order.save()