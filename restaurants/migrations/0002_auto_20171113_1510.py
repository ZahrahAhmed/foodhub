# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-11-13 15:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='restaurant',
            options={'ordering': ['name']},
        ),
        migrations.AddField(
            model_name='restaurant',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='restaurant_images'),
        ),
    ]