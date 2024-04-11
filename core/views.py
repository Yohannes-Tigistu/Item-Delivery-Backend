from rest_framework import mixins, viewsets, permissions, exceptions
from .models import *
from .serializers import *

class BankViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer

    

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(consumer=self.request.user.profile)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.consumer != request.user.profile:
            raise exceptions.PermissionDenied("You do not have permission to perform this action.")
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.consumer != request.user.profile:
            raise exceptions.PermissionDenied("You do not have permission to perform this action.")
        return super().destroy(request, *args, **kwargs)
    

class PaymentInvoiceViewSet(mixins.ListModelMixin,mixins.RetrieveModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):
    queryset = PaymentInvoice.objects.all()
    serializer_class = PaymentInvoiceSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.order.consumer != request.user.profile:
            raise exceptions.PermissionDenied("You do not have permission to perform this action.")
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.order.consumer != request.user.profile:
            raise exceptions.PermissionDenied("You do not have permission to perform this action.")
        return super().destroy(request, *args, **kwargs)
    
    
class ApproveDeliveryViewSet(mixins.ListModelMixin,mixins.RetrieveModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):
    queryset = ApproveDelivery.objects.all()
    serializer_class = ApproveDeliverySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.order.consumer != request.user.profile:
            raise exceptions.PermissionDenied("You do not have permission to perform this action.")
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.order.consumer != request.user.profile:
            raise exceptions.PermissionDenied("You do not have permission to perform this action.")
        return super().destroy(request, *args, **kwargs)
    
