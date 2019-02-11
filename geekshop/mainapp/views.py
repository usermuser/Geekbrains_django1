from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest, HttpResponseRedirect
from .models import Product, Category, Contacts
import datetime
import json

now = datetime.datetime.now()
cur_year = now.year


def index(request:HttpRequest):
    ctx = {'page_title': 'гЛаВная',
           'slider_big_text': 'удобные стулья',
           'date': cur_year,
           }
    return render(request, 'mainapp/index.html', ctx)


def products(request: HttpRequest):
    links = ['все', 'дом', 'офис', 'модерн', 'классика']
    ctx = {'page_title': 'каТалоГ',
           'links': links,
           'date': cur_year,
           }
    return render(request, 'mainapp/products.html', ctx)


def json_to_db(request: HttpRequest):

    Contacts.objects.all().delete()
    print('[+] All contacts deleted successfully')

    with open ('static/docs/location.json') as data:
        locations = json.load(data)

        for i in locations:
            new_contact = Contacts()
            new_contact.address = i['address']
            new_contact.phone_number = i['phone']
            new_contact.city = i['city']
            new_contact.email = i['email']
            new_contact.save()

    return HttpResponseRedirect('/')

def contacts(request: HttpRequest):
    contacts = Contacts.objects.all()
    ctx = {'locations': contacts,
           'page_title': 'Контакты',
           'date': cur_year,
           }
    return render(request, 'mainapp/contacts.html', ctx)


def categories(request: HttpRequest):
    categories = Category.objects.all()
    ctx = {'categories': categories}
    return render(request, 'mainapp/shop/categories.html', ctx)


def products_list(request: HttpRequest, category_slug=None):
    category = get_object_or_404(Category, slug=category_slug)
    products_list = Product.objects.filter(category=category)
    ctx = {'products_list': products_list, 'category': category}
    return render(request, 'mainapp/shop/products_list.html', ctx)


def product_details(request:HttpRequest, product_id=None):
    product = get_object_or_404(Product, id=product_id)
    ctx = {'product': product}
    return render(request, 'mainapp/shop/product_details.html', ctx)