from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import WishList

User = get_user_model()

class ProfileSerializer(serializers.ModelSerializer):
    
    # 내가 작성한 리뷰
    # 리뷰 좋아요

    class Meta:
        model = User
        fields = ('pk','username')




class WishListSerializer(serializers.ModelSerializer):

    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('pk','username',)

    user = UserSerializer(read_only=True)

    class Meta:
        model = WishList
        fields = '__all__'