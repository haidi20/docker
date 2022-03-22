import json
from unicodedata import category
from .serialize import CategorySerializer
from .views import PostView, CategoryView
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
    expectedResponseStatusCode = 201
    expectedResponseBody = requestBody
    expectedResponseBody["id"] = 1
    
    self.utils.assert_response(
      response,
      expectedResponseStatusCode,
      expectedResponseBody
    )
    
    
  def test_get_category(self):
    request = self.factory.get(
      self.uri
    )
    
    response = self.view(request)
    expectedResponseStatusCode = 200
    expectedResponseBody = [
      {
        "title": "education",
        "subTitle": "education about IT",
      }
    ]
    
    self.utils.assert_response(
      response,
      expectedResponseStatusCode,
      []
    )

class PostTestCase(APITestCase):
  def setUp(self):
    self.uri = "/post/"
    self.view = PostView.as_view()
    self.factory = APIRequestFactory()
    
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
      expected_response_status_code = 201
      
      self.assertEqual(
        response.status_code,
        expected_response_status_code,
      )
    
    
    
  def test_get_post(self):
    request = self.factory.get(
      self.uri
    )
    
    response = self.view(request)
    expected_response_status_code = 200
    
    self.assertEqual(
      response.status_code,
      expected_response_status_code
    )
    
class TestUtils(APITestCase):
  def assert_response(self, received_response, expected_status_code, expected_body):
      self.assertEqual(
          received_response.status_code,
          expected_status_code,
          'Expected response status code "{0}", received "{1}" instead.'.format(
              expected_status_code,
              received_response.status_code
          )
      )

      self.assertEqual(
          received_response.data,
          expected_body,
          'Expected response body "{0}", received "{1}" instead.'.format(
              expected_body,
              received_response.data
          )
      )
      
