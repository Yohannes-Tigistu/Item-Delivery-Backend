from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Profile
        fields = '__all__'


class ServiceProviderSeralizer(serializers.ModelSerializer):
    profile = ProfileSerializer
    class Meta:
        model =serviceProviders
        fields = '__all__'