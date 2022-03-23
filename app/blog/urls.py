from django.urls import re_path
from . import views
  
urlpatterns = [
  re_path(r'^category/$', views.getPostCategory, name="getPostCategory"),
  re_path(r'^category/(?P<pk>[0-9]+)$', views.findUpdateDeleteCategory, name="findUpdateDeleteCategory"),
]