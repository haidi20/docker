from django.http import Http404
from rest_framework.response import Response
from rest_framework import generics, status, views

from .models import Category, Post
from .serialize import CategorySerializer, PostSerializer

# Create your views here.

class PostView(generics.ListCreateAPIView):
  queryset = Post.objects.all()
  serializer_class = PostSerializer
  
  def get(self, request, *args, **kwargs):
    category = Post.objects.all()
    serializer = PostSerializer(category, many=True)
    
    return Response(serializer.data, status=status.HTTP_200_OK)
  
  def post(self, request, *args, **kwargs):
    serializer = PostSerializer(data=request.data)
    
    if serializer.is_valid():
      question = serializer.save()
      serializer = CategorySerializer(question)
      
      return Response(serializer.data, status=status.HTTP_201_CREATED)
      
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
  
class CategoryView(generics.ListCreateAPIView):
  queryset = Category.objects.all()
  serializer_class = CategorySerializer
  
  def get(self, request, *args, **kwargs):
    category = Category.objects.all()
    serializer = CategorySerializer(category, many=True)
    
    return Response(serializer.data, status=status.HTTP_200_OK)
  
  def post(self, request, *args, **kwargs):
    serializer = CategorySerializer(data=request.data)
    if serializer.is_valid():
      question = serializer.save()
      serializer = CategorySerializer(question)
      
      return Response(serializer.data, status=status.HTTP_201_CREATED)
      
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
