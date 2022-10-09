# Generated by Django 4.1.2 on 2022-10-09 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0006_alter_order_address_from_alter_order_address_to_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='address_from',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='order',
            name='address_to',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='order',
            name='count_list',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='order',
            name='is_delivered',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='order',
            name='is_pay',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_list',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='order',
            name='price',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='order',
            name='price_list',
            field=models.CharField(blank=True, max_length=1000),
        ),
    ]