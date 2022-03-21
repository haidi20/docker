import json
from unicodedata import category
from .models import Post, Category
from rest_framework import serializers
from django.contrib.postgres.fields import JSONField
        
class CategorySerializer(serializers.ModelSerializer):
  class Meta:
    model = Category
    fields = '__all__'
    
  
    
class PostSerializer(serializers.ModelSerializer):
  # category = serializers.SerializerMethodField("get_category")
  # category = serializers.StringRelatedField(many=False)
  # category = JSONField()
  category = CategorySerializer(many=False)
  
  class Meta:    
    model = Post
    fields = ("title", "content", "category_id", "category")
    extra_kwargs = {'category': {'read_only': True}}
    
  def get_title_category(self, category):
    if category:
      title = category.title
    
    return title
  
  def get_category(self, category):
    if category:
      return self.category