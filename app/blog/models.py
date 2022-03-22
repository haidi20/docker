from operator import mod
from django.db import models

# Create your models here.    
class Category(models.Model):
    title = models.CharField(max_length=50, null=True, blank=True)
    subTitle = models.CharField(max_length=100, null=True, blank=True)
    
class Post(models.Model):
    title = models.CharField(max_length=50, null=True, blank=True)
    content = models.TextField(max_length=200, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, null=True)
    
    class Meta:
        ordering = ['category']
