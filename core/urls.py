from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'banks', BankViewSet, basename='bank')
router.register(r'orders', OrderViewSet, basename='order')
router.register(r'payment-invoices', PaymentInvoiceViewSet, basename='invoice')
router.register(r'approve-delivery', ApproveDeliveryViewSet, basename='approve')

urlpatterns = router.urls