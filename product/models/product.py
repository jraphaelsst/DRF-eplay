from django.db import models

from .category import Category


class Product(models.Model):
    
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=500, blank=True, null=True)
    category = models.ManyToManyField(Category)
    active = models.BooleanField(default=True)
    price = models.FloatField(null=True)
