from django.http.response import JsonResponse
from rest_framework.renderers import JSONRenderer
from rest_framework import status
from rest_framework.decorators import api_view
from .blogSerialize import PostSerializer
from .models import Post

from blog.services import Services

# Create your views here.
@api_view(['GET'])
def post_index(request):
  posts = Post.objects.all()   
  
  if posts:
      data = PostSerializer(posts, many=True).data
      
      return JsonResponse(data, safe=False, status=status.HTTP_200_OK)
  else:
      return JsonResponse(status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def post_store(request):
  post = PostSerializer(data=request.data)
  
  if post.is_valid():
    post.save()
    
    return JsonResponse(post.data, status=status.HTTP_200_OK)
  else:
    return JsonResponse(status=status.HTTP_404_NOT_FOUND)
  
  # return JsonResponse(request.data, status=status.HTTP_200_OK) 

@api_view(['GET'])
def category_index(request):
  return JsonResponse({'message': "category index"}, status=status.HTTP_200_OK) 