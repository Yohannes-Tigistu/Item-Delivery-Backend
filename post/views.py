from django.shortcuts import render

from rest_framework import viewsets, permissions
from django_filters import rest_framework as filters

from .models import *
from .serialilzers import *


class IsServiceProvider(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.creator.profile.user == request.user
    
class CanEditPath(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.service.creator.profile.user == request.user
    
class ProductFilter(filters.FilterSet):

    class Meta:
        model = Service
        fields = {
            "paths__origin__name": ['contains',],
            "paths__destination__name": ['contains',]
        }

class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    permission_classes = [IsServiceProvider,permissions.IsAuthenticatedOrReadOnly]
    filterset_class = ProductFilter

    def get_serializer_class(self):
        if self.action == "create":
            return ServiceSerializer
        return ServiceListSerializer


class PathViewSet(viewsets.ModelViewSet):
    serializer_class = PathSerializer
    permission_classes = [CanEditPath, permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        service = self.kwargs.get('service_pk')
        return Path.objects.filter(service=service)