# Generated by Django 2.1.5 on 2019-01-18 15:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("notifications", "0009_announcement_from_group")]

    operations = [
        migrations.AlterField(
            model_name="announcement",
            name="from_group",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="from_group",
                to="users.AbakusGroup",
            ),
        )
    ]
