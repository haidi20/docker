from django.urls import re_path
from .api import categoryApi, postApi
  
urlpatterns = [
  # categories
  re_path(r'^category/$', categoryApi.getPostCategory, name="getPostCategory"),
  re_path(r'^category/(?P<pk>[0-9]+)$', categoryApi.findUpdateDeleteCategory, name="findUpdateDeleteCategory"),
  
  # posts
  re_path(r'^post/$', postApi.getPostPost, name="getPostPost"),
  re_path(r'^post/(?P<pk>[0-9]+)$', postApi.findUpdateDeletePost, name="findUpdateDeletePost"),
]