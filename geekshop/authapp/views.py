from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpResponse, HttpRequest

def redirect_to_login(request:HttpRequest   ):
    return HttpResponseRedirect('/auth/login')

def login(request:HttpRequest):
    title = 'войти на сайт'

    # 1. Создать форму для заполнения
    # 2. Проверить данные из запроса
    # 3. Выполнить аутентификацию

    return HttpResponse('auth/login')

def logout(request:HttpRequest):
    return HttpResponse('auth/logout')
