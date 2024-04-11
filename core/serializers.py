from rest_framework import serializers

from .models import *
from post.serialilzers import PathSerializer


class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bank
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    bank = BankSerializer(many=False, read_only=True)
    path = PathSerializer(read_only=True, many=True)
    class Meta:
        model = Order
        fields = '__all__'


class PaymentInvoiceSerializer(serializers.ModelSerializer):
    order = OrderSerializer(many=False, read_only=True)
    class Meta:
        model = PaymentInvoice
        fields = '__all__'


from rest_framework import serializers
from .models import *

class ApproveDeliverySerializer(serializers.ModelSerializer):
    order = OrderSerializer(many=False, read_only=True)
    
    class Meta:
        model = ApproveDelivery
        fields = '__all__'
