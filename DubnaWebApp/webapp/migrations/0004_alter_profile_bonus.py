# Generated by Django 4.1.2 on 2022-10-07 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_alter_profile_tg_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='bonus',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]