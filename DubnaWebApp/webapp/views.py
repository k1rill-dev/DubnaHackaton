from django.shortcuts import render
from cart.forms import *
from .models import *

def index(request):
    menu = Menu.objects.all()
    cart_product_form = CartAddProductForm()
    context = {
        "menu": menu,
        "cart_form": cart_product_form
    }
    return render(request, 'webapp/index.html', context)

def list_restaurants(request):
    return render(request, 'webapp/list_restaurants.html')

def menu(request):
    return render(request, 'webapp/menu.html')

def cart(request):
    return render(request, 'webapp/cart.html')
