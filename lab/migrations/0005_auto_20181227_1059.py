# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-12-27 02:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lab', '0004_auto_20181227_1044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sample',
            name='library_id',
            field=models.TextField(blank=True),
        ),
    ]
