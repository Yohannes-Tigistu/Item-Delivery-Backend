from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from .models import *

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


@receiver(post_save, sender=Order)
def create_approve_delivery(sender, instance, **kwargs):
    if instance.payment_completed:
        ApproveDelivery.objects.get_or_create(order=instance)


@receiver(post_save, sender=ApproveDelivery)
def update_order_status(sender, instance, **kwargs):
    if instance.consumer_approve and instance.paid and instance.provider_approve:
        order = instance.order
        order.status = 'completed'
        order.save()
    else:
        order = instance.order
        order.status = 'on_progress'
        order.save()
