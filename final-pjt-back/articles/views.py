from django.shortcuts import render
from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import  status
from .serializers import ReviewSerializer
from .models import Review

# Create your views here.


@api_view(['GET','POST'])
def review_list_create(request,movie_pk):

    if request.method == 'GET':
        reviews = get_list_or_404(Review)
        # 같은 movie id만 넘겨줘야하는 로직을 만들어야함

        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


    if request.method == 'POST':
        user = request.user
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=user)
            
            reviews = get_list_or_404(Review)
            serializer = ReviewSerializer(reviews, many=True)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['PUT'])
def review_update(request,movie_pk,review_pk):


    review = get_object_or_404(Review, pk=review_pk)
    print(review)

    if request.method == 'PUT':
        if request.user == review.user:
            print(request.user)
            print(review.user)




