from django.http import HttpRequest
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST

from django.shortcuts import render, get_object_or_404
from cart.forms import CartAddProductForm
from .models import *
from .forms import MakeOrder

def index(request):
    return render(request, 'webapp/index.html')


def list_restaurants(request):
    restiki = Restaurant.objects.all()
    context = {
        'restiki': restiki
    }
    return render(request, 'webapp/restiki.html', context)


def menu(request, restik):
    prod = Menu.objects.filter(restaurant=restik)
    cart_product_form = CartAddProductForm()
    return render(request, 'webapp/menu.html', {"prod": prod, 'cart_product_form': cart_product_form})


def order(request):
    if request.method == 'POST':
        form = MakeOrder(request.POST)
        if form.is_valid():
            form.save()
            return redirect('order')
    else:
        form = MakeOrder()
    return render(request, 'webapp/order.html', {'form': form})


def profile(request):
    return render(request, 'webapp/profile.html')
