from datetime import timezone
import datetime
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

""" Модель для публикации, содержит внешний ключ для автора """
class Post(models.Model):
    title = models.CharField(max_length=112, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Текст")
    image = models.ImageField(verbose_name="Фото", upload_to='images', blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор")

    def __str__(self):
        return self.title

""" Модель для комментария, содержит внешний ключ для автора и поста """    
class Comment(models.Model):
    content = models.TextField(verbose_name="Текст")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name="Публикация", null=True, blank=True, related_name='one')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор")

    def __str__(self):
        return self.content