from operator import mod
from django.db import models

# Create your models here.    
class Category(models.Model):
    title = models.CharField(max_length=20, null=True, blank=True)
    subTitle = models.CharField(max_length=10, null=True, blank=True)
    
    # json_content = JSONField()
    
    # def __str__(self):
    #     return f"title: {self.title}, subTitle: {self.subTitle}"
    
class Post(models.Model):
    title = models.CharField(max_length=20, null=True, blank=True)
    content = models.TextField(max_length=100, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, null=True)
    
    class Meta:
        ordering = ['category']
        
    def __str__(self):
        return self.title
