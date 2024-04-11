import uuid
from django.db import models
from post.models import *
from user.models import *

class Order(models.Model):
    consumer = models.ForeignKey(Profile, on_delete=models.DO_NOTHING, related_name='my_orders')
    service = models.ForeignKey(Service, on_delete=models.DO_NOTHING, related_name='orders')
    path = models.ManyToManyField(Path, related_name='order_path')
    created_at = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    approved = models.BooleanField(default=False)
    order_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)  # Unique order ID with token
