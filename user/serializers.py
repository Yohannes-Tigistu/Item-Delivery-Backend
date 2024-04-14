from rest_framework import serializers
from .models import *


class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class ProfileSerializer(serializers.ModelSerializer):
    user = UserModelSerializer(many=False, read_only=True)
    class Meta:
        model = Profile
        fields = '__all__'

class ProfileCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

class ServiceProviderSeralizer(serializers.ModelSerializer):
    creator = ProfileSerializer(many=False, read_only=True)
    class Meta:
        model = serviceProviders
        fields = '__all__'