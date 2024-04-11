from django.shortcuts import render

from rest_framework import viewsets, permissions

from .models import *
from .serialilzers import *


class IsServiceProvider(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.creator.profile.user == request.user
    
class CanEditPath(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.service.creator.profile.user == request.user

class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [IsServiceProvider,permissions.IsAuthenticatedOrReadOnly]


class PathViewSet(viewsets.ModelViewSet):
    serializer_class = PathSerializer
    permission_classes = [CanEditPath, permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        service = self.kwargs.get('service_pk')
        return Path.objects.filter(service=service)