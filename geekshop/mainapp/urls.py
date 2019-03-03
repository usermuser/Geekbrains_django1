from django.urls import path
from . import views

app_name = 'mainapp'

urlpatterns = [
    # http://127.0.0.1:8000/shop/
    # path('', views.categories, name='categories'),

    # http://127.0.0.1:8000/products
    path('', views.products, name='products'),

    # http://127.0.0.1:8000/shop/category/pechenki or chai (any category_slug)
    # path('category/<slug:category_slug>/', views.products_list, name='products'),

    # http://127.0.0.1:8000/products/1
    path('<int:product_id>/', views.products_list, name='products'),

    # path('product/<int:product_id>/', views.product_details, name='product_details'),

]
