import json
from .models import Post, Category
from rest_framework import serializers
        
class CategorySerializer(serializers.ModelSerializer):  
  class Meta:
    model = Category
    fields = '__all__'
    
class PostSerializer(serializers.ModelSerializer):
  # getCategory = serializers.SerializerMethodField("get_category")
  # category = serializers.StringRelatedField(many=False)
  # category = JSONField()
  category = CategorySerializer(many=False, read_only=True)
  
  class Meta:    
    model = Post
    fields = ("id", "title", "content", "category") 
    extra_kwargs = {'category': {'required': False, "allow_null": True}}
    # extra_kwargs = {'category': {'read_only': True}}
    
  def get_title_category(self, category):
    if category:
      title = category.title
    
    return title
  
  def get_category(self, category):
    if category:
      return json.dumps(category)