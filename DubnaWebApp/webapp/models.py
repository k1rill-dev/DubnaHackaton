from django.db import models


class Profile(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255, blank=True, null=True, verbose_name='ФИО')
    tg_username = models.CharField(max_length=255, blank=True, null=True, verbose_name='Юзернейм TG')
    tg_id = models.IntegerField(blank=True, null=True, default=0, verbose_name='Tg ID')
    address = models.CharField(blank=True, max_length=255, null=True, verbose_name='Адрес')
    bonus = models.IntegerField(blank=True, null=True, default=150, verbose_name='Бонусы')
    phone_number = models.BigIntegerField(blank=True, null=True, verbose_name='Номер телефона')
    is_stuff = models.BooleanField(default=False, blank=True, null=True, verbose_name='Является сотрудником')

    def __str__(self):
        return f"{self.tg_username}"

    class Meta:
        verbose_name = "Профиль"
        verbose_name_plural = "Профили"


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

class Stuff(models.Model):
    profile = models.IntegerField(blank=True, null=True, default=0, verbose_name='Tg ID')
    restaurant = models.ForeignKey("Restaurant", on_delete=models.PROTECT, blank=True, null=True,
                                   verbose_name='Ресторан')

    def __str__(self):
        return f"{self.profile.full_name} работает в {self.restaurant.title}"

    class Meta:
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"


class Order(models.Model):
    order_list = models.CharField(max_length=1000, blank=True, verbose_name='Список заказа')
    count_list = models.CharField(max_length=1000, blank=True, verbose_name='Кол-во штук в заказе')
    price_list = models.CharField(max_length=1000, blank=True, verbose_name='Цены')
    address_from = models.CharField(max_length=1000, blank=True, verbose_name='Адрес отправки')
    address_to = models.CharField(max_length=1000, blank=True, verbose_name='Адрес доставки')
    is_delivered = models.BooleanField(default=False, blank=True, verbose_name='Доставлено')
    is_pay = models.BooleanField(default=False, blank=True, verbose_name='Оплачено')
    price = models.CharField(max_length=1000, blank=True, verbose_name='Цена')
    comments = models.CharField(max_length=255, blank=True, null=True, verbose_name='Пожелания')
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Покупатель')
    date_of_create = models.DateTimeField(auto_now_add=True, blank=True, null=True, verbose_name='Дата создания')
    sale = models.IntegerField(blank=True, null=True, default=0, verbose_name='Скидка')
    restaurant = models.ForeignKey("Restaurant", on_delete=models.PROTECT, blank=True, null=True, verbose_name='Ресторан')

    def __str__(self):
        return f"{self.order_list[:10]}; {self.owner.tg_id}"
    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"


class Restaurant(models.Model):
    title = models.CharField(max_length=255, blank=True, verbose_name='Название')
    rating = models.FloatField(blank=True, verbose_name='Рейтинг')
    photo = models.ImageField(upload_to='restaurant_photos/%Y/%m/%d/', verbose_name='Фотографии', null=True, blank=True)
    address = models.CharField(max_length=255, blank=True, verbose_name='Адрес')

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "Ресторан"
        verbose_name_plural = "Рестораны"


class Menu(models.Model):
    title = models.CharField(max_length=255, blank=True, verbose_name='Название')
    description = models.CharField(max_length=255, blank=True, verbose_name='Описание')
    price = models.IntegerField(blank=True, verbose_name='Цена')
    photo = models.ImageField(upload_to='menu_photos/%Y/%m/%d/', verbose_name='Фотографии', null=True, blank=True)
    restaurant = models.ForeignKey("Restaurant", on_delete=models.PROTECT, verbose_name='Ресторан')
    category = models.ForeignKey("Category", on_delete=models.PROTECT, verbose_name='Категория')

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "Меню"
        verbose_name_plural = "Меню"


class Category(models.Model):
    title = models.CharField(max_length=255, blank=True, verbose_name='Категория')

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
