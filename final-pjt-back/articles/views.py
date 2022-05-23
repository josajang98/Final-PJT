from django.shortcuts import render
from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import  status
from .serializers import ReviewSerializer
from .models import Review

# Create your views here.

# 1. 토큰 값 없이 보내기 시도
# 2. 영화 하나에 하나의 리뷰만 사용할 수 있도록 수정
# 3. 평점 구현

@api_view(['GET','POST'])
def review_list_create(request,movie_pk):

    def seleted_movie(reviews, movie_pk):
        reviews_seleted_movie = []
        for review in reviews:
            if review.movie_id == movie_pk:
                reviews_seleted_movie.append(review)
        return reviews_seleted_movie

    
    # list
    if request.method == 'GET':
        reviews = get_list_or_404(Review)
        reviews_seleted_movie = seleted_movie(reviews, movie_pk)
        serializer = ReviewSerializer(reviews_seleted_movie, many=True) # many 값 뺼수 있으면 빼는걸로
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    # create
    elif request.method == 'POST':
        
        user = request.user
        review_list = Review.objects.all().filter(user_id=user)

        review_movie_list = []
        for review_ojt in review_list:
            review_movie_list.append(review_ojt.movie_id)
        
        if movie_pk in review_movie_list:
            data = {
                'exist':f'이미 작성하셨습니다'
            }
            return Response(data, status=status.HTTP_201_CREATED)

        else:
            serializer = ReviewSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save(user=user)
                reviews = get_list_or_404(Review)
                reviews_seleted_movie = seleted_movie(reviews, movie_pk)

                serializer = ReviewSerializer(reviews, many=True)
                return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['PUT','DELETE'])
def review_update_delete(request,movie_pk,review_pk):

    def seleted_movie(reviews, movie_pk):
        reviews_seleted_movie = []
        for review in reviews:
            if review.movie_id == movie_pk:
                reviews_seleted_movie.append(review)
        return reviews_seleted_movie

    review = get_object_or_404(Review, pk=review_pk)

    # update
    if request.method == 'PUT':
        if request.user == review.user:
            serializers = ReviewSerializer(instance=review, data=request.data)
            if serializers.is_valid(raise_exception=True):
                serializers.save()
                reviews = get_list_or_404(Review)
                reviews_seleted_movie = seleted_movie(reviews, movie_pk)

                serializers = ReviewSerializer(reviews_seleted_movie, many=True)
                return Response(serializers.data)

    # delete
    elif request.method == 'DELETE':
        if request.user == review.user:
            review.delete()
            reviews = get_list_or_404(Review)
            reviews_seleted_movie = seleted_movie(reviews, movie_pk)

            serializers = ReviewSerializer(reviews_seleted_movie, many=True)
            return Response(serializers.data)


@api_view(['POST'])
def like_review(request, movie_pk, review_pk):

    review = get_object_or_404(Review, pk=review_pk)
    user = request.user

    if review.like_users.filter(pk=user.pk).exists():
        review.like_users.remove(user)
    else:    
        review.like_users.add(user)
    
    serializers = ReviewSerializer(review)
    return Response(serializers.data)





