from django.urls import path
from .views import (
    UserListCreateView,
    UserDetailView,
    TagListCreateView,
    TagDetailView,
    PostListCreateView,
    PostDetailView,
    UserProfileView
)

urlpatterns = [
    # URL для списка и создания пользователей
    path('users/', UserListCreateView.as_view(), name='user-list-create'),
    # URL для получения, обновления и удаления конкретного пользователя
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),

    # URL для списка и создания тегов
    path('tags/', TagListCreateView.as_view(), name='tag-list-create'),
    # URL для получения, обновления и удаления конкретного тега
    path('tags/<int:pk>/', TagDetailView.as_view(), name='tag-detail'),

    # URL для списка и создания постов
    path('posts/', PostListCreateView.as_view(), name='post-list-create'),
    # URL для получения, обновления и удаления конкретного поста
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),

    # URL для получения, создания, обновления и удаления профиля пользователя
    path('users/<int:user_id>/profile/', UserProfileView.as_view(), name='user-profile'),
]
