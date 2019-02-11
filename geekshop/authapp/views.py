from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpResponse, HttpRequest
from .forms import LoginForm, RegisterForm, UpdateForm
from django.contrib import auth
from django.urls import reverse

def redirect_to_login(request: HttpRequest):
    return HttpResponseRedirect('/auth/login')

def login(request: HttpRequest):
    title = 'войти на сайт'

    # 1. Создать форму для заполнения

    login_form = LoginForm(data=request.POST)

    # 2. Проверить данные из запроса

    if request.method == 'POST' and login_form.is_valid():
        login = request.POST['username']
        password = request.POST['password']

        # 3. Выполнить аутентификацию

        user = auth.authenticate(username=login, password=password)


        if user and user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect('/')

    ctx = {
        'title': title,
        'login_form': login_form,
    }
    return render(request, 'authapp/login.html', ctx)


def logout(request: HttpRequest):
    auth.logout(request)
    return HttpResponseRedirect('/')


def edit(request: HttpRequest):
    title = 'редактировать профиль'

    # 1. Создать рег форму для заполнения, перед этим импортируй

    if request.method == 'POST':
        update_form = UpdateForm(request.POST, instance=request.user)

        # 2. Проверить данные из запроса
        if update_form.is_valid():
            # 3. Сохранение при регистрации
            update_form.save()

            return HttpResponseRedirect(reverse('auth:edit'))

    else:
        update_form = UpdateForm(instance=request.user)

    ctx = {
        'title': title,
        'update_form': update_form,
    }
    return render(request, 'authapp/edit.html', ctx)

def register(request: HttpRequest):
    title = 'регистрация'

    # 1. Создать рег форму для заполнения, перед этим импортируй

    if request.method == 'POST':
        register_form = RegisterForm(request.POST)

        # 2. Проверить данные из запроса
        if register_form.is_valid():

            # 3. Сохранение при регистрации
            register_form.save()

            return HttpResponseRedirect(reverse('auth:login'))

    else:
        register_form = RegisterForm()

    ctx = {
        'title': title,
        'reg_form': register_form,
    }
    return render(request, 'authapp/register.html', ctx)





