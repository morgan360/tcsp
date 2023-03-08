from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from orders.models import Order
from lessons.models import Product, Term
from swimmer.models import Swimling


# Create your models here.
class Booking(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                             blank=True, null=True, )
    swimling = models.ForeignKey(Swimling, on_delete=models.CASCADE,blank=True, null=True,)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product,
                                related_name='products',
                                on_delete=models.CASCADE)
    term = models.ForeignKey(Term, on_delete=models.CASCADE)
    activated = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    changed_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='changers', blank=True, null=True,)

    class Meta:
        ordering = ['-created']
        indexes = [
            models.Index(fields=['-created']),
        ]

    def __str__(self):
        return f'Order {self.id}'