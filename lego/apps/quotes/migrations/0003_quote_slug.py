# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-29 12:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0002_remove_quote_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='quote',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
    ]
