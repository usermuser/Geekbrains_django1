from django.db import models
from django.core.validators import RegexValidator

class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Имя')
    slug = models.SlugField(max_length=100, db_index=True, unique=True, verbose_name='Ссылка')

    class Meta:
        ordering = ['name']
        verbose_name = 'категория'
        verbose_name_plural = 'категории'

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category,
                                 on_delete=models.CASCADE,
                                 related_name='products',
                                 verbose_name='Категория'
                                 )

    name = models.CharField(max_length=100, db_index=True, verbose_name='Имя')
    slug = models.SlugField(max_length=100, db_index=True, verbose_name='Ссылка')
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)
        verbose_name = 'товар'
        verbose_name_plural = 'товары'

    def __str__(self):
        return self.name


class Contacts(models.Model):

    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    # validators should be a list

    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    email = models.EmailField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'контакт'
        verbose_name_plural = 'контакты'

    def __str__(self):
        return 'Contacts in ' + self.city
