from django.contrib import admin
from .models import *

@admin.register(Bank)
class BankAdmin(admin.ModelAdmin):
    list_display = ['bank_name', 'account_number']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_id', 'consumer', 'service', 'total_price', 'approved', 'payment_completed']
    list_filter = ['approved', 'payment_completed']
    search_fields = ['order_id', 'consumer__username', 'service__content']
    readonly_fields = ['final_price']

@admin.register(PaymentInvoice)
class PaymentInvoiceAdmin(admin.ModelAdmin):
    list_display = ['order', 'payment_date', 'is_paid']
    list_filter = ['is_paid']
    search_fields = ['order__order_id']

@admin.register(ApproveDelivery)
class ApproveDeliveryAdmin(admin.ModelAdmin):
    list_display = ['order', 'provider_approve', 'consumer_approve']
    list_filter = ['provider_approve', 'consumer_approve']
    search_fields = ['order__order_id']
