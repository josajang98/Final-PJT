from rest_framework import serializers
from django.contrib.auth import get_user_model

from articles.views import like_review
from .models import WishList
from articles.models import Review

User = get_user_model()

class ProfileSerializer(serializers.ModelSerializer):
    
    class ReviewSerializer(serializers.ModelSerializer):
        class UserSerializer(serializers.ModelSerializer):
            class Meta:
                model = User
                fields = ('pk', 'username')

        user =  UserSerializer(read_only=True)
        like_users_count = serializers.IntegerField(source='like_users.count',read_only=True)

        class Meta:
            model = Review
            fields = '__all__'

    like_review = ReviewSerializer(many=True, read_only=True)
    review_set = ReviewSerializer(many=True, read_only=True)
    review_count = serializers.IntegerField(source='review_set.count',read_only=True)

    class Meta:
        model = User
        fields = ('pk','username','review_set','review_count','like_review','genre_id',)


class WishListSerializer(serializers.ModelSerializer):

    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('pk','username',)

    user = UserSerializer(read_only=True)

    class Meta:
        model = WishList
        fields = '__all__'