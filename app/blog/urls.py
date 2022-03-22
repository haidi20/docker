from django.urls import include, re_path
from .views import PostView, CategoryView
  
urlpatterns = [
  re_path(r'^post/', PostView.as_view(), name="post"),
  re_path(r'^category/', CategoryView.as_view(), name="category")
]