from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('list_restaurants/', list_restaurants, name='list_restaurants'),
    path('menu/<int:restik>/', menu, name='menu'),
    # path('menu/<int:restik>', menu, name='menu'),
    path('order', order, name='order'),
    # path('profile/', profile, name='profile')
]
