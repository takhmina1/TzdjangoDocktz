from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import User, UserProfile, Tag, Post
from .serializers import UserSerializer, UserProfileSerializer, TagSerializer, PostSerializer
from django.shortcuts import get_object_or_404

# Представление для списка пользователей и создания нового пользователя
class UserListCreateView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Представление для получения, обновления и удаления пользователя
class UserDetailView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Представление для списка тегов и создания нового тега
class TagListCreateView(ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

# Представление для получения, обновления и удаления тега
class TagDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

# Представление для списка постов и создания нового поста
class PostListCreateView(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

# Представление для получения, обновления и удаления поста
class PostDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

# Представление для профиля пользователя (OneToOne)
class UserProfileView(APIView):
    def get(self, request, user_id):
        profile = get_object_or_404(UserProfile, user__id=user_id)
        serializer = UserProfileSerializer(profile)
        return Response(serializer.data)


    def post(self, request):
        serializer = UserProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def put(self, request, user_id):
        profile = get_object_or_404(UserProfile, user__id=user_id)
        serializer = UserProfileSerializer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, user_id):
        profile = get_object_or_404(UserProfile, user__id=user_id)
        profile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
