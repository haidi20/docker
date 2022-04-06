import json
from django.test import Client
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.core.paginator import Paginator

from .Utils import TestUtils
from ..models import Category, Post
from ..serializes import CategorySerializer, PostSerializer

# initialize the APIClient app
client = Client()

class PostTestCase(APITestCase):
  def setUp(self):
    self.uri = "/category/"
    self.utils = TestUtils()
    self.initialData = {
      "title": "education",
      "content": "lksjdfdf",
    }
    self.updateData = {
      "title": "education",
      "content": "klsdjf",
    }
    
  def test_all(self):
    # get API response
    responses = client.get(reverse('getPostPost'), {"page": 1})
    # get data from db
    posts = Post.objects.get_queryset().order_by('id')
    paginator = Paginator(posts, 10)  # 3 posts in each page
    page = 1
    
    categoryPagination = paginator.page(page)
    
    expectedBody = PostSerializer(categoryPagination, many=True).data
    
    self.utils.assert_responses(
      responses,
      status.HTTP_200_OK,
      expectedBody
    )
    
  def test_create(self):  
    findCategory = self.utils.create_category_if_not_exists()
    categorySerialize = CategorySerializer(findCategory, many=False).data
    
    self.initialData["category_id"] = categorySerialize["id"]
      
    responses = client.post(
      reverse('getPostPost'),
      json.dumps(self.initialData),
      content_type="application/json",
    )
    
    # get data from db
    category = Post.objects.last()
    expectedBody = PostSerializer(category, many=False).data
    
    self.utils.assert_responses(
      responses,
      status.HTTP_201_CREATED,
      expectedBody
    )
  
  def test_update(self):    
    createPost = self.utils.create_post_if_not_exists()
    
    self.updateData["category_id"] = createPost.category_id
    
    responses = client.put(
      reverse('findUpdateDeletePost',  kwargs={'pk': createPost.id}),
      json.dumps(self.updateData),
      content_type="application/json",
    )
    
    # get data from db
    category = Post.objects.get(id=createPost.id)
    expectedBody = PostSerializer(category, many=False).data
    
    self.utils.assert_responses(
      responses,
      status.HTTP_204_NO_CONTENT,
      expectedBody
    )
    
  def test_delete(self):
    createPost = self.utils.create_post_if_not_exists()
    
    responses = client.delete(
      reverse('findUpdateDeletePost',  kwargs={'pk': createPost.id})
    )
    
    self.utils.assert_responses(
      responses,
      status.HTTP_204_NO_CONTENT,
    )