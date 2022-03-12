from django.shortcuts import render
from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status

from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET'])
def index(request):
  return JsonResponse({'message': 'post index'}, status=status.HTTP_200_OK) 