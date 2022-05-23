from rest_framework import serializers
from django.contrib.auth import get_user_model

from articles.views import like_review
from .models import WishList
from articles.models import Review

User = get_user_model()





class ProfileSerializer(serializers.ModelSerializer):
    
    class ReviewSerializer(serializers.ModelSerializer):
        class Meta:
            model = Review
            # fields = '__all__'
            fields = ('pk','title','content','rate','user')

    
    like_review = ReviewSerializer(many=True, read_only=True)
    like_review_count = serializers.IntegerField(source='like_review.count',read_only=True)


    review_set = ReviewSerializer(many=True, read_only=True)
    review_count = serializers.IntegerField(source='review_set.count',read_only=True)

    class Meta:
        model = User
        # fields = '__all__'
        fields = ('pk','username','review_set','review_count','like_review','like_review_count','genre_id',)



class WishListSerializer(serializers.ModelSerializer):

    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('pk','username',)

    user = UserSerializer(read_only=True)

    class Meta:
        model = WishList
        fields = '__all__'