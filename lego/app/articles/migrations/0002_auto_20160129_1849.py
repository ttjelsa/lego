# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-29 18:49
from __future__ import unicode_literals

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='article',
            managers=[
                ('public_objects', django.db.models.manager.Manager()),
            ],
        ),
    ]
