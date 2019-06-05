from django.db import models

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