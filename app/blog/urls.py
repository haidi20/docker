
from django.urls import path
from . import views
  
urlpatterns = [
  path("post/", views.post_index),
  path("post/store", views.post_store),
  path("category/", views.category_index),
]