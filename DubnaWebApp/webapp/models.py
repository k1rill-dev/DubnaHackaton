from decimal import Decimal

from dj_shop_cart.cart import CartItem
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    tg_username = models.CharField(max_length=255, blank=False)
    tg_id = models.IntegerField(blank=False)

    def __str__(self):
        return f"{self.tg_username}"

#signals to User model
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Order(models.Model):
    order_list = models.CharField(max_length=255, blank=True)
    restaurant = models.ForeignKey("Restaurant", on_delete=models.CASCADE)
    address_to_deliver = models.CharField(max_length=255, blank=True)
    is_delivered = models.BooleanField(default=False, blank=True)
    price = models.IntegerField(blank=True)
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.order_list[:10]}; {self.owner.tg_username}"

class Restaurant(models.Model):
    title = models.CharField(max_length=255, blank=True)
    rating = models.FloatField(blank=True)
    address = models.CharField(max_length=255, blank=True)
    menu = models.ForeignKey("Menu", on_delete=models.PROTECT)

class Menu(models.Model):
    title = models.CharField(max_length=255, blank=True)
    description = models.CharField(max_length=255, blank=True)
    category = models.ForeignKey("Category", on_delete=models.PROTECT)

    def get_price(self, item: CartItem) -> Decimal:
        """The only requirements of the dj_shop_cart package apart from the fact that the products you add
        to the cart must be instances of django based models. You can use a different name for this method
        but be sure to update the corresponding setting (see Configuration). Even if you change the name the
        function signature should match this one.
        """


class Category(models.Model):
    title = models.CharField(max_length=255, blank=True)