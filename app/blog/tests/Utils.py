from rest_framework.test import APITestCase

from ..models import Category, Post
from ..serializes import CategorySerializer, PostSerializer


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
        "test body"
      )    
  
  def create_category_if_not_exists(self, title="IT", subTitle="thing all about IT"):
    category = Category.objects.create(
      title=title,
      subTitle=subTitle
    )
    
    return category
  
  def create_post_if_not_exists(self, title="growth world IT", content="ksdjflksdjfkj"):
    category = self.create_category_if_not_exists()
    serializeCategory = CategorySerializer(category, many=False)
    
    post = Post.objects.create(
      title=title,
      content=content,
      category_id=serializeCategory.data["id"]
    )
    
    return post