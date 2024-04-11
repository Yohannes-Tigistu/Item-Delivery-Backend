from django.contrib import admin
from .models import Bank, Order, PaymentInvoice

@admin.register(Bank)
class BankAdmin(admin.ModelAdmin):
    list_display = ['bank_name', 'account_number']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_id', 'consumer', 'service', 'created_at', 'total_price', 'approved']
    list_filter = ['created_at', 'approved']
    search_fields = ['order_id', 'consumer__username']

@admin.register(PaymentInvoice)
class PaymentInvoiceAdmin(admin.ModelAdmin):
    list_display = ['order', 'payment_date', 'transaction_id', 'is_paid']
    list_filter = ['payment_date', 'is_paid']
    search_fields = ['order__order_id']
