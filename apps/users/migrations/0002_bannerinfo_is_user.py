# Generated by Django 2.2.1 on 2020-08-01 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bannerinfo',
            name='is_user',
            field=models.BooleanField(default=False, verbose_name='是否为用户登录所用'),
        ),
    ]
