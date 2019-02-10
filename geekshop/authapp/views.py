from django.shortcuts import render
from django.http import HttpResponse


def login(request:HttpResponse):
    return HttpResponse('auth/login')

def logout(request:HttpResponse):
    return HttpResponse('auth/logout')
