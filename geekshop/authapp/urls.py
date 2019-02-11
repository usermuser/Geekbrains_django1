from django.urls import path
from . import views

app_name = 'authapp'

urlpatterns = [

    # http://127.0.0.1:8000/auth redirect to auth/login
    path('', views.redirect_to_login, name='index'),

    # http://127.0.0.1:8000/auth/login
    path('login/', views.login, name='login'),

    # http://127.0.0.1:8000/auth/logout
    path('logout/', views.logout, name='logout'),

    path('edit/', views.edit, name='edit'),  # edit user data
]