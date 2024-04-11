import decimal
from django.db import models
from django.conf import settings
from user.models import serviceProviders, Profile

class City(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Service(models.Model):
    creator = models.ForeignKey(serviceProviders, on_delete=models.SET_NULL, null=True, related_name='posts')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    views = models.ManyToManyField(Profile, related_name='post_views', blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    
    def __str__(self):
        return f"Post by {self.creator.profile.user.username} at {self.created_at}"

class Path(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    origin = models.ForeignKey(City, on_delete=models.SET_NULL, null=True, related_name='origins')
    destination = models.ForeignKey(City, on_delete=models.SET_NULL, null=True, related_name='destinations')
    updated_at = models.DateTimeField(auto_now=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
    departur_time = models.DateTimeField()
    estimated_arrival_time = models.DateTimeField()
