from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpResponse, HttpRequest
from .forms import LoginForm
from django.contrib import auth

def redirect_to_login(request:HttpRequest):
    return HttpResponseRedirect('/auth/login')

def login(request:HttpRequest):
    title = 'войти на сайт'

    # 1. Создать форму для заполнения

    login_form = LoginForm(data=request.POST)

    # 2. Проверить данные из запроса

    if request.method == 'POST' and login_form.is_valid():
        login = request.POST['username']
        password = request.POST['password']

        # 3. Выполнить аутентификацию

        user = auth.authenticate(username=login, password=password)

        # 3.1 Сохранение при регистрации
        #RegisterForm.save()

        if user and user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect('/')

    ctx = {
        'title': title,
        'login_form': login_form,
    }
    return render(request, 'authapp/login.html', ctx)


def logout(request:HttpRequest):
    auth.logout(request)
    return HttpResponseRedirect('/')
