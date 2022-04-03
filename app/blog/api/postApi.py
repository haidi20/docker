from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from ..models import Post
from ..serializes import PostSerializer

# Create your views here.  
@api_view(['GET', 'POST'])
def getPostPost(request):  
  #get all post
  if request.method == "GET":
    categories = Post.objects.get_queryset().order_by('id')
    paginator = Paginator(categories, 10)  # 3 posts in each page
    page = request.GET.get('page')
    
    try:
      postList = paginator.page(page)
    except PageNotAnInteger:
           
      postList = paginator.page(1)
    except EmptyPage:
      postList = paginator.page(paginator.num_pages)
    
    serialize = PostSerializer(postList, many=True).data
    
    return Response(data=serialize, status=status.HTTP_200_OK)
  
  #insert new post
  if request.method == "POST":
    # data = {
    #     'title': request.data.get('title'),
    #     'subTitle': request.data.get('subTitle'),
    # }
    serializer = PostSerializer(data=request.data)
    
    if serializer.is_valid():
      serializer.save()
    
      return Response(serializer.data, status=status.HTTP_201_CREATED)
      
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'DELETE', 'PUT'])
def findUpdateDeletePost(request, pk):
  try:
    post = Post.objects.get(pk=pk)
  except Post.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)

  # get details of a single post
  if request.method == 'GET':
    serializer = PostSerializer(post)
    return Response(serializer.data)

  # update details of a single post
  if request.method == 'PUT':
    serializer = PostSerializer(post, data=request.data)
    
    if serializer.is_valid():
      serializer.save() 
      
      return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
      
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  # delete a single post
  if request.method == 'DELETE':
    post.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
  
  
    
