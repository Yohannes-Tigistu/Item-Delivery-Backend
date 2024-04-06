import decimal
from django.db import models
from django.conf import settings

# Create your models here.

user_model = settings.AUTH_USER_MODEL

class Post(models.Model):
    creator = models.ForeignKey(user_model, on_delete=models.DO_NOTHING, related_name='posts')
    content = models.TextField()
    origin = models.CharField(max_length=256)
    destination = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    departur_time = models.DateTimeField()
    estimated_arrival_time = models.DateTimeField()
    views = models.ManyToManyField(user_model, related_name='post_views')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    customers = models.ManyToManyField(user_model, related_name="post_customers")

    @property
    def final_price(self):
        return (self.price) * decimal(0.9)
    
    def __str__(self):
        return f"Post by {self.user.username} at {self.created_at}"


