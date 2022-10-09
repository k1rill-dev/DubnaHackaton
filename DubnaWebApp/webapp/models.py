from django.db import models


class Profile(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255, blank=True, null=True)
    tg_username = models.CharField(max_length=255, blank=True, null=True)
    tg_id = models.IntegerField(blank=True, null=True, default=0)
    address = models.CharField(blank=True, max_length=255, null=True)
    bonus = models.IntegerField(blank=True, null=True, default=0)
    phone_number = models.BigIntegerField(blank=True, null=True)
    is_stuff = models.BooleanField(default=False, blank=True, null=True)

    def __str__(self):
        return f"{self.tg_username}"


# signals to User model
# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)
#
#
# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()


class Order(models.Model):
    order_list = models.CharField(max_length=1000, blank=True)
    count_list = models.CharField(max_length=1000, blank=True)
    price_list = models.CharField(max_length=1000, blank=True)
    address_from = models.CharField(max_length=1000, blank=True)
    address_to = models.CharField(max_length=1000, blank=True)
    is_delivered = models.BooleanField(default=False, blank=True)
    is_pay = models.BooleanField(default=False, blank=True)
    price = models.CharField(max_length=1000, blank=True)
    comments = models.CharField(max_length=255, blank=True, null=True)
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True, null=True)
    date_of_create = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return f"{self.order_list[:10]}; {self.owner.tg_id}"


class Restaurant(models.Model):
    title = models.CharField(max_length=255, blank=True)
    rating = models.FloatField(blank=True)
    address = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"{self.title}"


class Menu(models.Model):
    title = models.CharField(max_length=255, blank=True)
    description = models.CharField(max_length=255, blank=True)
    price = models.IntegerField(blank=True)
    restaurant = models.ForeignKey("Restaurant", on_delete=models.PROTECT)
    category = models.ForeignKey("Category", on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.title}"


class Category(models.Model):
    title = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"{self.title}"
