from django.urls import path
from . import views
  
urlpatterns = [
  path("category/", views.category_index),
  path("post/", views.post_index),
  path("post/store", views.post_store),
]