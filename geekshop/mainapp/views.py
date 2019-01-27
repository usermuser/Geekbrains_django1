from django.shortcuts import render
from django.http import HttpRequest
import datetime
import json
# locations = [
# {'city':'Moscow', 'address':1111, 'email':'ema11', 'phone':'ph23'},
# {'city':'Chelyabinsk', 'address':22, 'email':'ema11', 'phone':'ph23'},
# {'city':'Chelyabinsk', 'address':22, 'email':'ema11', 'phone':'ph23'},
# ]

now = datetime.datetime.now()
cur_year = now.year

def index(request:HttpRequest):
    ctx = {'page_title':'гЛаВная',
           'slider_big_text':'удобные стулья',
           'date':cur_year,
           }
    return render(request, 'mainapp/index.html', ctx)

def products(request:HttpRequest):
    links = ['все','дом','офис','модерн','классика']
    ctx = {'page_title':'каТалоГ',
           'links':links,
           'date': cur_year,
           }
    return render(request, 'mainapp/products.html', ctx)

def contacts(request:HttpRequest):
    with open ('static/docs/location.json') as data:
        locations = json.load(data)

    ctx = {'page_title':'кОнтактЫ',
           'date': cur_year,
           'locations':locations,
           }
    return render(request, 'mainapp/contacts.html', ctx)
