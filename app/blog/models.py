from operator import mod
from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=20, null=True)
    content = models.TextField(max_length=100, null=True)
    category = models.PositiveIntegerField(null=False, default=0)
    
class Category(models.Model):
    title = models.CharField(max_length=20)
