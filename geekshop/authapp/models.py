from django.db import models
from django.contrib.auth.models import AbstractUser

class ShopUser(AbstractUser):

    age = models.PositiveIntegerField(verbose_name='возраст', default=0)
    avatar = models.ImageField(upload_to='users_avatars',
                               verbose_name='аватар',
                               blank=True)
