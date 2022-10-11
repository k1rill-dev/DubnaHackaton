from django.shortcuts import redirect

from django.shortcuts import render

from cart.cart import Cart
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
            cd = form.cleaned_data
            cart = Cart(request)
            a = [i for i in cart]
            quantity = [i['quantity'] for i in a]
            price = [float(i['price']) for i in a]
            product = [str(i['product']) for i in a]
            product_query = [i['product'] for i in a]
            total_price = [float(i['total_price']) for i in a]
            res_address = [i['product'].restaurant.address for i in a]

            p = Profile.objects.last()
            bonus_count = 0
            if cd['is_bonus'] and p.bonus > 0:
                bonus_count = p.bonus
                p.bonus -= bonus_count
                p.save()

            Order.objects.create(order_list=product, count_list=quantity, price_list=price, address_from=res_address,
                                 address_to=cd['address'], price=total_price, comments=cd['comments'],
                                 restaurant=product_query[0].restaurant, owner=p, sale=bonus_count
                                 )
            return redirect('order')
    else:
        form = MakeOrder()
    return render(request, 'webapp/order.html', {'form': form, 'bonus': Profile.objects.last().bonus})


# def profile(request):
#     Profile.objects.get()
#     return render(request, 'webapp/profile.html')
