# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-12-19 05:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lab', '0028_auto_20181219_1150'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sample',
            name='people',
        ),
    ]
