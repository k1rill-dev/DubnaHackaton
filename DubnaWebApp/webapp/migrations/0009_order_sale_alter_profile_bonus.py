# Generated by Django 4.1.2 on 2022-10-10 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0008_order_restaurant_alter_profile_address_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='sale',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='bonus',
            field=models.IntegerField(blank=True, default=150, null=True),
        ),
    ]
