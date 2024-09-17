from django.contrib import admin
from .models import User, UserProfile, Tag, Post

# Регистрация модели пользователя
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'created_at')
    search_fields = ('username', 'email')
    list_filter = ('created_at',)

# Регистрация модели профиля пользователя
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio')
    search_fields = ('user__username', 'bio')

# Регистрация модели тега
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

# Регистрация модели поста
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'get_tags')
    search_fields = ('title', 'content', 'author__username')
    list_filter = ('author', 'tags')
    
    # Функция для отображения тегов в виде строки
    def get_tags(self, obj):
        return ", ".join([tag.name for tag in obj.tags.all()])
    get_tags.short_description = 'Tags'
