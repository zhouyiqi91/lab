# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-12-26 05:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lab', '0005_auto_20181226_1341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sample',
            name='xiaji',
            field=models.BooleanField(choices=[(True, '\u662f'), (False, '\u5426')], default=False),
        ),
    ]
