# Generated by Django 4.1.2 on 2022-10-09 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_order_price_list_alter_order_count_list_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='restaurant',
        ),
        migrations.AddField(
            model_name='order',
            name='address_from',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AddField(
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
            name='order_list',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='order',
            name='price_list',
            field=models.CharField(blank=True, max_length=1000),
        ),
    ]
