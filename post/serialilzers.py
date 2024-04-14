from rest_framework import serializers

from .models import *
from user.serializers import ServiceProviderSeralizer, ProfileSerializer


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'

class PathSerializer(serializers.ModelSerializer):
    class Meta:
        model = Path
        fields = '__all__'