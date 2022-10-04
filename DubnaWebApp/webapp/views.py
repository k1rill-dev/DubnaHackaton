from dj_shop_cart.cart import get_cart_class
from django.http import HttpRequest
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST
from .models import *
from .forms import *


Cart = get_cart_class()


@require_POST
def add_product(request: HttpRequest, product_id: int):
    product = get_object_or_404(Menu.objects.all(), pk=product_id)
    quantity = int(request.POST.get("quantity"))
    cart = Cart.new(request)
    cart.add(product, quantity=quantity)
    return redirect("cart")


@require_POST
def remove_product(request: HttpRequest):
    item_id = request.POST.get("item_id")
    quantity = int(request.POST.get("quantity"))
    cart = Cart.new(request)
    cart.remove(item_id=item_id, quantity=quantity)
    return redirect("cart")


@require_POST
def empty_cart(request: HttpRequest):
    Cart.new(request).empty()
    return redirect("cart")


def index(request):
    menu = Menu.objects.all()
    cart_product_form = CartAddProductForm
    return render(request, 'webapp/index.html', {"menu":menu, "cart_product_form": cart_product_form})


def list_restaurants(request):
    return render(request, 'webapp/list_restaurants.html')


def menu(request):
    return render(request, 'webapp/menu.html')


def cart(request):
    return render(request, 'webapp/cart.html', {"cart": Cart.new(request)})
