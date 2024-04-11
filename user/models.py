from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

from phonenumber_field.modelfields import PhoneNumberField

user_model = settings.AUTH_USER_MODEL


class User(AbstractUser):
    first_name = models.CharField(max_length=150, blank=False)
    last_name = models.CharField(max_length=150, blank=False)
    email = models.EmailField(blank=False, unique=True)

    REQUIRED_FIELDS = ['first_name', 'last_name', 'email']

class Profile(models.Model):
    user = models.OneToOneField(user_model,on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to="user/profile", blank=True)
    bio = models.TextField(blank=True)
    phone_number = PhoneNumberField(blank=True, region="ET")
    def __str__(self) -> str:
        return f"{self.user.username}'s Profile"

class serviceProviders(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE, related_name='service_provider')
    id_front = models.FileField(upload_to='user/id', blank=True)
    id_back = models.FileField(upload_to='user/id', blank=True)
    fayda_number = models.CharField(max_length=255, null=True, blank=True)
    id_verified = models.BooleanField(default=False)

    bank_account1 = models.CharField(max_length=255, blank=True)
    bank_account2 = models.CharField(max_length=255, blank=True)
    grand_father_name = models.CharField(max_length=255, blank=True)

    
    def __str__(self) -> str:
        return f"Service Provider: {self.profile.user.username}"
