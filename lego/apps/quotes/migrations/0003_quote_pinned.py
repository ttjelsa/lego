# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-19 14:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0002_auto_20170903_2206'),
    ]

    operations = [
        migrations.AddField(
            model_name='quote',
            name='pinned',
            field=models.BooleanField(default=False),
        ),
    ]