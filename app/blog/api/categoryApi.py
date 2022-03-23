from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from ..models import Category
from ..serializes import CategorySerializer

# Create your views here.  
@api_view(['GET', 'POST'])
def getPostCategory(request):  
  #get all category
  if request.method == "GET":
    categories = Category.objects.get_queryset().order_by('id')
    paginator = Paginator(categories, 10)  # 3 posts in each page
    page = request.GET.get('page')
    
    try:
      categoryList = paginator.page(page)
    except PageNotAnInteger:
           
      categoryList = paginator.page(1)
    except EmptyPage:
      categoryList = paginator.page(paginator.num_pages)
    
    serialize = CategorySerializer(categoryList, many=True).data
    
    return Response(data=serialize, status=status.HTTP_200_OK)
  
  #insert new category
  if request.method == "POST":
    # data = {
    #     'title': request.data.get('title'),
    #     'subTitle': request.data.get('subTitle'),
    # }
    serializer = CategorySerializer(data=request.data)
    
    if serializer.is_valid():
        serializer.save()
      
        return Response(serializer.data, status=status.HTTP_201_CREATED)
      
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'DELETE', 'PUT'])
def findUpdateDeleteCategory(request, pk):
  try:
      category = Category.objects.get(pk=pk)
  except Category.DoesNotExist:
      return Response(status=status.HTTP_404_NOT_FOUND)

  # get details of a single category
  if request.method == 'GET':
      serializer = CategorySerializer(category)
      return Response(serializer.data)

  # update details of a single category
  if request.method == 'PUT':
      serializer = CategorySerializer(category, data=request.data)
      if serializer.is_valid():
          serializer.save()
          return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  # delete a single category
  if request.method == 'DELETE':
    category.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
  
  
    
