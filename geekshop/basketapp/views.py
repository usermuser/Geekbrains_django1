from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest, HttpResponseRedirect
from mainapp.models import Product
from basketapp.models import Basket


def add(request: HttpRequest, id: int):
    product = get_object_or_404(Product, pk=id)

    exists_item = Basket.objects.filter(product__id=id) # user_id тоже понадобится

    if exists_item:
        exists_item[0].quantity += 1
        exists_item[0].save()
    else:
        new_item = Basket(user=request.user, product=product)
        new_item.quantity = 1
        new_item.save()

    return HttpResponseRedirect(request.META['HTTP_REFERER']) # SERVER VARS


def remove(request: HttpRequest, id: int):
    pass


def index(request: HttpRequest):
    pass

