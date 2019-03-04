from django.urls import path
from . import views

app_name = 'mainapp'

urlpatterns = [
    # http://127.0.0.1:8000/shop/
    # path('', views.categories, name='categories'),

    # http://127.0.0.1:8000/products
    path('', views.products, name='index'),

    # http://127.0.0.1:8000/shop/category/pechenki or chai (any category_slug)
    # path('category/<slug:category_slug>/', views.products_list, name='products'),

    # http://127.0.0.1:8000/products/1
    path('<int:id>/', views.products, name='products'), # {% url 'mainapp:products' id=1 %}

    # http://127.0.0.1:8000/products/details/1
    path('details/<int:id>/', views.product_details, name='details'), # {% url 'mainapp:details' id=1 %}

    # path('product/<int:product_id>/', views.product_details, name='product_details'), # old_code

]
