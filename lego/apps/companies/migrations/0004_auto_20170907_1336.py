# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-07 13:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0003_auto_20170830_1646'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='company',
            name='admin_comment',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]