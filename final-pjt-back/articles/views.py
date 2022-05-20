from django.shortcuts import render
from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import  status
from .serializers import ReviewSerializer
from .models import Review

# Create your views here.


@api_view(['POST'])
def review_create(request):

    user = request.user
    serializer = ReviewSerializer(data=request.data)

    if serializer.is_valid(raise_exception=True):
        serializer.save(user=user)
        
        reviews = get_list_or_404(Review)
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)



def review_update(reauest,):
    pass





