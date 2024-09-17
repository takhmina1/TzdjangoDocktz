from rest_framework import serializers
from .models import User, UserProfile, Tag, Post

# Сериализатор для модели пользователя
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'created_at']

# Сериализатор для модели профиля пользователя
class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()  # Вложенный сериализатор для связанного пользователя

    class Meta:
        model = UserProfile
        fields = ['user', 'bio']

# Сериализатор для модели тега
class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']

# Сериализатор для модели поста
class PostSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)  # Вложенный сериализатор для тегов
    author = UserSerializer()  # Вложенный сериализатор для автора

    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'tags', 'author']

















# # Сериализатор для пользователя
# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['id', 'name', 'email']

# # Сериализатор для профиля пользователя (один к одному)
# class UserProfileSerializer(serializers.ModelSerializer):
#     user = UserSerializer()

#     class Meta:
#         model = UserProfile
#         fields = ['user', 'address', 'phone_number']

# # Сериализатор для заказа (один ко многим)
# class OrderSerializer(serializers.ModelSerializer):
#     user = UserSerializer()

#     class Meta:
#         model = Order
#         fields = ['id', 'user', 'order_date', 'total_amount']

# # Сериализатор для товара (многие ко многим)
# class ProductSerializer(serializers.ModelSerializer):
#     users = UserSerializer(many=True)

#     class Meta:
#         model = Product
#         fields = ['id', 'name', 'description', 'price', 'users']
