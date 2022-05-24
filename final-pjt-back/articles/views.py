from django.shortcuts import render
from django.shortcuts import get_list_or_404, get_object_or_404
from django.contrib.auth import get_user_model
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import  status
from .serializers import ReviewSerializer, UserSerializer
from .models import Review
User = get_user_model()

# Create your views here.

# 1. 토큰 값 없이 보내기 시도
# 2. 영화 하나에 하나의 리뷰만 사용할 수 있도록 수정
# 3. 평점 구현
# 4. 평점 default = 0

@api_view(['GET','POST'])
def review_list_create(request,movie_pk):

    def seleted_movie(reviews, movie_pk):
        reviews_selected_movie = []
        for review in reviews:
            if review.movie_id == movie_pk:
                reviews_selected_movie.append(review)
        return reviews_selected_movie

    def rate_selected_movie(reviews, movie_pk):
        rate_selected_movie = []
        for review in reviews:
            if review.movie_id == movie_pk:
                rate_selected_movie.append(review.rate)
        return rate_selected_movie

    # list
    if request.method == 'GET':
        reviews = get_list_or_404(Review)
        reviews_selected_movie = seleted_movie(reviews, movie_pk)
        rate_list = rate_selected_movie(reviews, movie_pk)
        average_rate = round(sum(rate_list)/len(rate_list),1)
        serializer = ReviewSerializer(reviews_selected_movie, many=True)
        data={
            'serializer_data':serializer.data,
            'average_rate':average_rate
        }
        return Response(data, status=status.HTTP_201_CREATED)

    # create
    elif request.method == 'POST':
        user = request.user
        review_list = Review.objects.all().filter(user_id=user)

        # movie_id 모음
        review_movie_list = []
        for review_ojt in review_list:
            review_movie_list.append(review_ojt.movie_id)
        
        # 작성되어 있을시 data보냄
        if movie_pk in review_movie_list:
            data = {
                'exist':f'이미 작성하셨습니다'
            }
            return Response(data, status=status.HTTP_201_CREATED)

        # 작성 안되어 있을시 저장
        else:
            serializer = ReviewSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save(user=user)
                reviews = get_list_or_404(Review)
                reviews_selected_movie = seleted_movie(reviews, movie_pk)
                serializer = ReviewSerializer(reviews_selected_movie, many=True)
                return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['PUT','DELETE'])
def review_update_delete(request,movie_pk,review_pk):

    def seleted_movie(reviews, movie_pk):
        reviews_selected_movie = []
        for review in reviews:
            if review.movie_id == movie_pk:
                reviews_selected_movie.append(review)
        return reviews_selected_movie

    review = get_object_or_404(Review, pk=review_pk)

    # update
    if request.method == 'PUT':
        if request.user == review.user:
            serializers = ReviewSerializer(instance=review, data=request.data)
            if serializers.is_valid(raise_exception=True):
                serializers.save()
                reviews = get_list_or_404(Review)
                reviews_selected_movie = seleted_movie(reviews, movie_pk)

                serializers = ReviewSerializer(reviews_selected_movie, many=True)
                return Response(serializers.data)

    # delete
    elif request.method == 'DELETE':
        if request.user == review.user:
            review.delete()
            reviews = get_list_or_404(Review)
            reviews_selected_movie = seleted_movie(reviews, movie_pk)

            serializers = ReviewSerializer(reviews_selected_movie, many=True)
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


@api_view(['POST'])
def genre_save(request, genre_pk):

    user = get_object_or_404(User,pk=request.user.pk)
    serializers = UserSerializer(instance=user, data=request.data)
    if serializers.is_valid(raise_exception=True):
        serializers.save(genre_id=genre_pk)
        return Response(serializers.data)





