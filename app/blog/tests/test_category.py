import json
from django.test import Client
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.core.paginator import Paginator

from .Utils import TestUtils
from ..models import Category
from ..serializes import CategorySerializer

# initialize the APIClient app
client = Client()

class CategoryTestCase(APITestCase):
  def setUp(self):
    self.uri = "/category/"
    self.utils = TestUtils()
    self.category = self.utils.create_category_if_not_exists()
    self.initialData = {
      "title": "education",
      "subTitle": "education school",
    }
    self.updateData = {
      "title": "education",
      "subTitle": "education school sports",
    }
    
  def test_all(self):
    # get API response
    responses = client.get(reverse('getPostCategory'), {"page": 1})
    # get data from db
    categories = Category.objects.get_queryset().order_by('id')
    paginator = Paginator(categories, 10)  # 3 posts in each page
    page = 1
    
    categoryPagination = paginator.page(page)
    
    expectedBody = CategorySerializer(categoryPagination, many=True).data
    
    self.utils.assert_responses(
      responses,
      status.HTTP_200_OK,
      expectedBody
    )
    
  def test_create(self):    
    responses = client.post(
      reverse('getPostCategory'),
      json.dumps(self.initialData),
      content_type="application/json",
    )
    
    # get data from db
    category = Category.objects.last()
    expectedBody = CategorySerializer(category, many=False).data
    
    self.utils.assert_responses(
      responses,
      status.HTTP_201_CREATED,
      expectedBody
    )
  
  def test_update(self):
    # getCategory = self.category
    createCategory = Category.objects.create(
      title=self.initialData["title"],
      subTitle=self.initialData["subTitle"],
    )
    # getCategory.title = "change title"
    
    responses = client.put(
      reverse('findUpdateDeleteCategory',  kwargs={'pk': createCategory.id}),
      json.dumps(self.updateData),
      content_type="application/json",
    )
    
    # get data from db
    category = Category.objects.get(id=createCategory.id)
    expectedBody = CategorySerializer(category, many=False).data
    
    self.utils.assert_responses(
      responses,
      status.HTTP_204_NO_CONTENT,
      expectedBody
    )
    
  def test_delete(self):
    createCategory = Category.objects.create(
      title=self.initialData["title"],
      subTitle=self.initialData["subTitle"],
    )
    
    responses = client.delete(
      reverse('findUpdateDeleteCategory',  kwargs={'pk': createCategory.id})
    )
    
    self.utils.assert_responses(
      responses,
      status.HTTP_204_NO_CONTENT,
    )