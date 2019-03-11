from django.urls import path

from basketapp import views

app_name = 'basketapp'


urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.basket, name='show_basket'),
    path('add/<int:id>/', views.add, name='add'),
    path('remove/<int:id>/', views.remove, name='remove'),


]
