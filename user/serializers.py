from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False, read_only=True)
    class Meta:
        model = Profile
        fields = '__all__'


class ServiceProviderSeralizer(serializers.ModelSerializer):
    creator = ProfileSerializer(many=False, read_only=True)
    class Meta:
        model = serviceProviders
        fields = '__all__'