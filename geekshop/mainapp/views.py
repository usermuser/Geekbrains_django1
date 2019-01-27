from django.shortcuts import render
from django.http import HttpRequest
import datetime


def index(request:HttpRequest):
    now = datetime.datetime.now()
    cur_year = now.year
    ctx = {'page_title':'гЛаВная',
           'slider_big_text':'удобные стулья',
           'date':cur_year,}
    return render(request, 'mainapp/index.html', ctx)

def products(request:HttpRequest):
    links = ['все','дом','офис','модерн','классика']
    ctx = {'page_title':'каТалоГ',
           'links':links}
    return render(request, 'mainapp/products.html', ctx)

def contacts(request:HttpRequest):
    ctx = {'page_title':'кОнтактЫ'}
    return render(request, 'mainapp/contacts.html', ctx)
