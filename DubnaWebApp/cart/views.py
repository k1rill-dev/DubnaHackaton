from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from webapp.models import Menu
from .cart import Cart
from .forms import *


@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Menu, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Menu, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')


@require_POST
def cart_upd(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Menu, id=product_id)
    form = CartUpdProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=1,
                 update_quantity=False)
    return redirect('cart:cart_detail')


@require_POST
def cart_minus(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Menu, id=product_id)
    form = CartUpdProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=1,
                 update_quantity=False,
                 minus=True)
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    cart_product_form = CartUpdProductForm()
    comment_form = CommentForm()
    # print([i for i in cart])
    return render(request, 'cart/cart.html',
                  {'cart': cart, 'cart_product_form': cart_product_form, 'comment_form': comment_form})
