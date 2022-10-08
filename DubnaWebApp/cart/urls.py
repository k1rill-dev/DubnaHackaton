from django.urls import re_path

from . import views

urlpatterns = [
    re_path(r'^$', views.cart_detail, name='cart_detail'),
    re_path(r'^add/(?P<product_id>\d+)/$', views.cart_add, name='cart_add'),
    re_path(r'^remove/(?P<product_id>\d+)/$', views.cart_remove, name='cart_remove'),
    re_path(r'^plus/(?P<product_id>\d+)/$', views.cart_upd, name='cart_plus'),
    re_path(r'^minus/(?P<product_id>\d+)/$', views.cart_minus, name='cart_minus'),
]
