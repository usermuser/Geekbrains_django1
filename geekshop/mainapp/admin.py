from django.contrib import admin

from .models import Product, Category

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','category','slug','price','stock','available')
    prepopulated_fields = {'slug':('name',)}

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','slug')
    #list_filter = ['']
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)

