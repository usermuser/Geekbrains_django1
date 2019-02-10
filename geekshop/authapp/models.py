from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):

    age = models.PositiveIntegerField(verbose_name='возраст')
    avatar = models.ImageField(upload_to='users_avatars/%Y/%m/%d',
                               verbose_name='аватар',
                               blank=True)