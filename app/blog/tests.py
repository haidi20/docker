import json
from collections import OrderedDict
from unicodedata import category
from .serialize import CategorySerializer
from .views import PostView, CategoryView
from rest_framework import generics, renderers, serializers, status
from rest_framework.test import APITestCase
from rest_framework.test import APIRequestFactory

from .models import Category, Post

# Create your tests here.

class CategoryTestCase(APITestCase):
  def setUp(self):
    self.uri = "/category/"
    self.view = CategoryView.as_view()
    self.factory = APIRequestFactory()
    self.utils = TestUtils()
    
  def test_create_category(self):
    requestBody = {
      "title": "education",
      "subTitle": "education about IT",
    }
    
    request = self.factory.post(
      self.uri,
      json.dumps(requestBody),
      content_type='application/json'
    )
    
    response = self.view(request)
    
    self.assertEquals(
      response.status_code,
      status.HTTP_201_CREATED
    )
    
  def test_create_category_fail(self):
    requestBody = {}
    
    request = self.factory.post(
      self.uri,
      json.dumps(requestBody),
      content_type='application/json'
    )
    
    response = self.view(request)
    
    self.assertEquals(
      response.status_code,
      status.HTTP_400_BAD_REQUEST
    )
    
    
  def test_get_category(self):      
    request = self.factory.get(
      self.uri
    )  
    
    response = self.view(request)
    
    self.assertEquals(
      response.status_code,
      status.HTTP_200_OK,
    )
    

class PostTestCase(APITestCase):
  def setUp(self):
    self.uri = "/post/"
    self.view = PostView.as_view()
    self.factory = APIRequestFactory()
    self.utils = TestUtils()
    self.category = self.utils.create_category_if_not_exists()
    
  def test_create_post(self):
    findCategory = Category.objects.last()
    category = CategorySerializer(data=findCategory, many=False)
    
    if category.is_valid():
      request_body = {
        "title": "become developer",
        "subTitle": "slkdjflskjdfklsjfdlksjdf",
        "category": category.data["id"],
      }
      
      request = self.factory.post(
        self.uri,
        json.dumps(request_body),
        content_type='application/json'
      )
      
      response = self.view(request)
      
      self.assertEquals(
        response.status_code,
        status.HTTP_201_CREATED,
      )
      
  def test_create_post_fail(self):    
    request_body = {}
      
    request = self.factory.post(
      self.uri,
      json.dumps(request_body),
      content_type='application/json'
    )
    
    response = self.view(request)
    
    self.assertEquals(
      response.status_code,
      status.HTTP_400_BAD_REQUEST,
      f"response = {response.status_code}"
    )   
    
    
  def test_get_post(self):
    request = self.factory.get(
      self.uri
    )
    
    response = self.view(request)
    
    self.assertEquals(
      response.status_code,
      status.HTTP_200_OK
    )
    
class TestUtils(APITestCase):
  def assert_response(self, received_response, expected_status_code, expected_body = None):
    self.assertEqual(
        received_response.status_code,
        expected_status_code,
        'Expected response status code "{0}", received "{1}" instead.'.format(
            expected_status_code,
            received_response.status_code
        )
    )
    
    if expected_body is not None:    
      # responseData = json.dumps(received_response.data)  
      responseData = received_response.data
      self.assertEqual(
          responseData,
          expected_body,
          'Expected response body "{0}", received "{1}" instead.'.format(
              expected_body,
              responseData
          )
      )
  
  
  @staticmethod
  def create_category_if_not_exists(title="IT", subTitle="thing all about IT"):
    category = Category.objects.create(
      title=title,
      subTitle=subTitle
    )
    
    return category
      
