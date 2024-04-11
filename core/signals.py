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
