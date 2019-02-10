from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpResponse, HttpRequest

def redirect_to_login(request:HttpRequest   ):
    return HttpResponseRedirect('/auth/login')

def login(request:HttpRequest):
    return HttpResponse('auth/login')

def logout(request:HttpRequest):
    return HttpResponse('auth/logout')
