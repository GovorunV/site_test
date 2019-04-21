from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here. создание таблице
class News(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    avtor = models.ForeignKey(User, on_delete=models.CASCADE) #в автор подставляем с таблици юзерс
