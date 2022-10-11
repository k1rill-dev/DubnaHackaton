from django.contrib import admin
from .models import *


class MenuAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', 'restaurant', 'category')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'restaurant', 'category')
    list_editable = ('price',)

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'order_list', 'price', 'owner', 'restaurant', 'is_delivered', 'is_pay')
    list_display_links = ('id',)
    search_fields = ('title', 'restaurant', 'owner')
    list_editable = ('is_delivered', 'is_pay')

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('tg_id', 'full_name', 'tg_username', 'address', 'bonus', 'is_stuff')
    list_display_links = ('tg_id', 'tg_username')
    search_fields = ('tg_username', 'full_name', 'address')
    list_editable = ('is_stuff',)


class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'rating', 'address')
    list_display_links = ('id', 'title')
    search_fields = ('title', )
    list_editable = ('rating',)

admin.site.register(Menu, MenuAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Category)
admin.site.register(Restaurant, RestaurantAdmin)
admin.site.register(Stuff)
