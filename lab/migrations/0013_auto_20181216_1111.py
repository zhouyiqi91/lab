# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-12-16 03:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lab', '0012_auto_20181216_1102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sample',
            name='AATI',
            field=models.ImageField(blank=True, upload_to='static'),
        ),
    ]