from django.db import models

# Модель пользователя
class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username

# Модель профиля пользователя (один к одному)
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()

# Модель тега (многие ко многим)
class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

# Модель поста (многие к одному)
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    tags = models.ManyToManyField(Tag)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title







# drugoy primer

# # Один к одному (OneToOneField): связь между пользователем и его профилем
# class UserProfile(models.Model):
#     user = models.OneToOneField('User', on_delete=models.CASCADE)
#     address = models.CharField(max_length=255)
#     phone_number = models.CharField(max_length=20)

#     def __str__(self):
#         return f'{self.user.name} - Profile'

# # Один ко многим (ForeignKey): один пользователь может иметь много заказов
# class Order(models.Model):
#     user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='orders')
#     order_date = models.DateField()
#     total_amount = models.DecimalField(max_digits=10, decimal_places=2)

#     def __str__(self):
#         return f'Order #{self.id} by {self.user.name}'
#     def __str__(self):
#         return self.name

# # Пользовательская модель для примера
# class User(models.Model):
#     name = models.CharField(max_length=100)
#     email = models.EmailField(unique=True)

#     def __str__(self):
#         return self.name
