# Generated by Django 4.1.2 on 2022-10-11 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0011_stuff'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stuff',
            name='profile',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Tg ID'),
        ),
    ]
