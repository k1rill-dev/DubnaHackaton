from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('list_restaurants', list_restaurants, name='list_restaurants'),
    path('menu', menu, name='menu'),
]