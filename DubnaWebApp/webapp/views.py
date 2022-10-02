from django.shortcuts import render

def index(request):
    return render(request, 'webapp/index.html')

def list_restaurants(request):
    return render(request, 'webapp/list_restaurants.html')

def menu(request):
    return render(request, 'webapp/menu.html')

def cart(request):
    return render(request, 'webapp/cart.html')