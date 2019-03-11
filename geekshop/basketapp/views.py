from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest, HttpResponseRedirect
from mainapp.models import Product
from basketapp.models import Basket


def basket(request: HttpRequest):
    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)

    ctx = {
        'page_title': 'Basket',
        'basket': basket,
    }
    return render(request, 'basketapp/basket.html', ctx)

# THIS CODE IS FROM WEBINAR AND IT IS WORKING

# def add(request: HttpRequest, id: int):
#     product = get_object_or_404(Product, pk=id)
#
#     exists_item = Basket.objects.filter(product__id=id) # user_id тоже понадобится
#
#     if exists_item:
#         exists_item[0].quantity += 1
#         exists_item[0].save()
#     else:
#         new_item = Basket(user=request.user, product=product)
#         new_item.quantity = 1
#         new_item.save()
#
#     return HttpResponseRedirect(request.META['HTTP_REFERER']) # SERVER VARS

# THIS CODE IS FROM GEEKBRAINS LESSON 5 TUTORIAL
#####################################################


def add(request: HttpRequest, id: int):
    product = get_object_or_404(Product, pk=id)

    basket = Basket.objects.filter(user=request.user, product=product).first()

    if not basket:
        basket = Basket(user=request.user, product=product)

    basket.quantity += 1
    basket.save()

    return HttpResponseRedirect(request.META['HTTP_REFERER'])

#####################################################


def remove(request: HttpRequest, id: int):
    ctx = {}
    return render(request, 'basketapp/basket.html', ctx)


def index(request: HttpRequest):
    pass

