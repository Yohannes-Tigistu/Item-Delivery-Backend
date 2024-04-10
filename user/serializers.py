from rest_framework import serializers
from .models import *


class GetProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id','user', 'profile_pic', 'bio', 'phone_number']
