
from django.db.models import fields
from rest_framework import serializers
from .models import Post, Category
  
class PostSerializer(serializers.ModelSerializer):
  class Meta:
    model = Post
    fields = ("title", "content", "category")
        
class CategorySerializer(serializers.ModelSerializer):
  class Meta:
    model = Category
    fields = ("title")