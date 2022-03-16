from django.shortcuts import render
from django.shortcuts import render
from django.http.response import JsonResponse
from grpc import services
from rest_framework.parsers import JSONParser 
from rest_framework import status

from rest_framework.decorators import api_view

from blog.services import Services

# Create your views here.
@api_view(['GET'])
def post_index(request):
  services = Services()
  
  postIndex = services.post_index()
  
  return JsonResponse({'message': postIndex}, status=status.HTTP_200_OK) 