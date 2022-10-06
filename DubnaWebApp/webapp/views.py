from dj_shop_cart.cart import get_cart_class
from django.http import HttpRequest
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST

from cart.forms import CartAddProductForm
from .models import *

def index(request):
    product = get_object_or_404(Menu,
                                id=1)
    cart_product_form = CartAddProductForm()
    return render(request, 'webapp/index.html', {'product': product,
                                                        'cart_product_form': cart_product_form})


def list_restaurants(request):
    return render(request, 'webapp/list_restaurants.html')


def menu(request):
    return render(request, 'webapp/menu.html')


def cart(request):
    return render(request, 'webapp/cart.html', {"cart": Cart.new(request)})
