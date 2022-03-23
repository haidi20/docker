import json
from venv import create
from django.urls import reverse
from django.test import TestCase, Client
from rest_framework.test import APITestCase
from rest_framework import status
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from .models import Category, Post
from .serialize import CategorySerializer, PostSerializer

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
  
class TestUtils(APITestCase):
  
  def assert_responses(self, responses, expectedStatusCode, expectedBody = None):
    self.assertEqual(
      responses.status_code,
      expectedStatusCode,
      f"response: {responses.data}"
    )
    
    if expectedBody is not None:
      self.assertEqual(
        responses.data,
        expectedBody,
        "test data"
      )    
  
  @staticmethod
  def create_category_if_not_exists(title="IT", subTitle="thing all about IT"):
    category = Category.objects.create(
      title=title,
      subTitle=subTitle
    )
    
    # serialize = CategorySerializer(category, many=False).data
    
    return category
  
  @staticmethod
  def create_post_if_not_exists(title="growth world IT", content="ksdjflksdjfkj"):
    category = Category.objects.last()
    serializeCategory = CategorySerializer(category, many=False)
    
    post = Post.objects.create(
      title=title,
      content=content,
      category=serializeCategory.data["id"]
    )
    
    return post