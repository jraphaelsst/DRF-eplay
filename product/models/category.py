from django.db import models


class Category(models.Model):
    
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, blank=False, null=False)
    description = models.TextField(max_length=500)
    active = models.BooleanField(default=True)
