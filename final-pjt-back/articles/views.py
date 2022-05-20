from django.shortcuts import render
from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import  status
from .serializers import ReviewSerializer
from .models import Review

# Create your views here.


@api_view(['POST'])
def review_create(request, movie_pk):

    user = request.user
    serializer = ReviewSerializer(data=request.data)
    reviews = get_object_or_404(Review)

    if serializer.is_valid(raise_exception=True):
        serializer.save(movie_pk=movie_pk, user=user)
        
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)



def review_update(reauest,):
    pass





