from django.shortcuts import get_list_or_404, get_object_or_404
from django.contrib.auth import get_user_model

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import ProfileSerializer, WishListSerializer
from .models import WishList


User = get_user_model()

@api_view(['GET'])
def profile(request, username):

    if request.user.username == username:
        user = get_object_or_404(User, username=username)
        serializer = ProfileSerializer(user)
        return Response(serializer.data)

    else:
        data={
            'Notyou' : '당신의 프로필이 아닙니다'
        }
        return Response(data)


@api_view(['GET','POST'])
def wishlist_show_save(request):
    
    # show
    if request.method == 'GET':
        user = request.user
        wish_list = get_list_or_404(WishList,user_id=user)
        serializers = WishListSerializer(wish_list, many=True)
        return Response(serializers.data)

    # save
    elif request.method == 'POST':
        
        user = request.user
        movie_id = int(request.data['movie_id'])
        wish_list = WishList.objects.all().filter(user_id=user)

        # 위시무비 id 값만 불러오기
        wish_movie_id = []
        for wish in wish_list:
            wish_movie_id.append(wish.movie_id)

        # wish_movie_id값안에 값이 있으면 ==> 삭제
        if movie_id in wish_movie_id:
            wish_object = get_object_or_404(WishList,user_id=user,movie_id=movie_id)
            wish_object.delete()
            wish_list = WishList.objects.all().filter(user_id=user)
            serializers = WishListSerializer(wish_list, many=True)
            return Response(serializers.data)

        # 없으면 ==> 추가
        else:
            serializers = WishListSerializer(data=request.data)
            if serializers.is_valid(raise_exception=True):
                serializers.save(user=user)
                wish_list = WishList.objects.all().filter(user_id=user)
                serializers = WishListSerializer(wish_list, many=True)
                return Response(serializers.data)
