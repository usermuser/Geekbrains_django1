from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest, HttpResponseRedirect, HttpResponse
from .models import Product, Category, Contacts
from basketapp.models import Basket
import datetime
import json

now = datetime.datetime.now()
cur_year = now.year


def index(request:HttpRequest):
    basket = Basket.objects.filter(user=request.user)
    ctx = {'page_title': 'гЛаВная',
           'slider_big_text': 'удобные стулья',
           'date': cur_year,
           'basket': basket,
           }
    return render(request, 'mainapp/index.html', ctx)


def products(request: HttpRequest, id=None):
    title = 'продукты'
    links_menu = Category.objects.all()
    basket = Basket.objects.filter(user=request.user)


    if id is not None:
        same_products = Product.objects.filter(category__pk=id)
    else:
        same_products = Product.objects.all()

    ctx = {'page_title': title,
           'links': links_menu,
           'date': cur_year,
           'same_products': same_products,
           'basket': basket,
           }
    return render(request, 'mainapp/products.html', ctx)


def product_details(request: HttpRequest, id=None):
    # request.session['test'] = 1011110;
    # request.session.flush()

    if id is not None:
        item = get_object_or_404(Product, id=id)
        same_products = Product.objects.exclude(pk=id).filter(category__pk=item.category_id)
        links_menu = Category.objects.all()

        ctx = {
                'page_title': 'Товар: {}'.format(item.name),
                'same_products': same_products,
                'links': links_menu,
                'item': item,
        }

        return render(request, 'mainapp/details.html', ctx)

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


# this code has been written as homework for lesson2 or 3, i don't remember,
# for now we don't need it
'''
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
'''
