from django.urls import path


from basketapp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/<int:id>/', views.add, name='add'),
    path('remove/<int:id>/', views.remove, name='remove'),


]
