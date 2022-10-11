# Generated by Django 4.1.2 on 2022-10-11 06:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0009_order_sale_alter_profile_bonus'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterModelOptions(
            name='menu',
            options={'verbose_name': 'Меню', 'verbose_name_plural': 'Меню'},
        ),
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name': 'Заказ', 'verbose_name_plural': 'Заказы'},
        ),
        migrations.AlterModelOptions(
            name='profile',
            options={'verbose_name': 'Профиль', 'verbose_name_plural': 'Профили'},
        ),
        migrations.AlterModelOptions(
            name='restaurant',
            options={'verbose_name': 'Ресторан', 'verbose_name_plural': 'Рестораны'},
        ),
        migrations.AddField(
            model_name='menu',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='menu_photos/%Y/%m/%d/', verbose_name='Фотографии'),
        ),
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(blank=True, max_length=255, verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='menu',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='webapp.category', verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='menu',
            name='description',
            field=models.CharField(blank=True, max_length=255, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='menu',
            name='price',
            field=models.IntegerField(blank=True, verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='menu',
            name='restaurant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='webapp.restaurant', verbose_name='Ресторан'),
        ),
        migrations.AlterField(
            model_name='menu',
            name='title',
            field=models.CharField(blank=True, max_length=255, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='order',
            name='address_from',
            field=models.CharField(blank=True, max_length=1000, verbose_name='Адрес отправки'),
        ),
        migrations.AlterField(
            model_name='order',
            name='address_to',
            field=models.CharField(blank=True, max_length=1000, verbose_name='Адрес доставки'),
        ),
        migrations.AlterField(
            model_name='order',
            name='comments',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Пожелания'),
        ),
        migrations.AlterField(
            model_name='order',
            name='count_list',
            field=models.CharField(blank=True, max_length=1000, verbose_name='Кол-во штук в заказе'),
        ),
        migrations.AlterField(
            model_name='order',
            name='date_of_create',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='order',
            name='is_delivered',
            field=models.BooleanField(blank=True, default=False, verbose_name='Доставлено'),
        ),
        migrations.AlterField(
            model_name='order',
            name='is_pay',
            field=models.BooleanField(blank=True, default=False, verbose_name='Оплачено'),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_list',
            field=models.CharField(blank=True, max_length=1000, verbose_name='Список заказа'),
        ),
        migrations.AlterField(
            model_name='order',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='webapp.profile', verbose_name='Покупатель'),
        ),
        migrations.AlterField(
            model_name='order',
            name='price',
            field=models.CharField(blank=True, max_length=1000, verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='order',
            name='price_list',
            field=models.CharField(blank=True, max_length=1000, verbose_name='Цены'),
        ),
        migrations.AlterField(
            model_name='order',
            name='restaurant',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='webapp.restaurant', verbose_name='Ресторан'),
        ),
        migrations.AlterField(
            model_name='order',
            name='sale',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Скидка'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='address',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Адрес'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='bonus',
            field=models.IntegerField(blank=True, default=150, null=True, verbose_name='Бонусы'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='full_name',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='ФИО'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='is_stuff',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='Является сотрудником'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone_number',
            field=models.BigIntegerField(blank=True, null=True, verbose_name='Номер телефона'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='tg_id',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Tg ID'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='tg_username',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Юзернейм TG'),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='address',
            field=models.CharField(blank=True, max_length=255, verbose_name='Адрес'),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='rating',
            field=models.FloatField(blank=True, verbose_name='Рейтинг'),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='title',
            field=models.CharField(blank=True, max_length=255, verbose_name='Название'),
        ),
    ]