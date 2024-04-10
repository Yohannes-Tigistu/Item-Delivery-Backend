from django.shortcuts import get_object_or_404
from rest_framework import viewsets, mixins, permissions
from .models import Profile
from .serializers import GetProfileSerializer


class IsProfileOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user

class ProfileViewSet(mixins.CreateModelMixin ,mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    queryset = Profile.objects.all()
    serializer_class = GetProfileSerializer
    lookup_field = 'user_id'
    permission_classes = [IsProfileOwner, permissions.IsAuthenticatedOrReadOnly] 

    def get_object(self):
        user_id = self.kwargs.get('user_id')  
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, user_id=user_id)
        self.check_object_permissions(self.request, obj)
        return obj
