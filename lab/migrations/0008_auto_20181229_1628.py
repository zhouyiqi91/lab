# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-12-29 08:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lab', '0007_auto_20181229_1623'),
    ]

    operations = [
        migrations.AddField(
            model_name='sample',
            name='fenxi',
            field=models.BooleanField(default=False, verbose_name='\u5206\u6790'),
        ),
        migrations.AlterField(
            model_name='sample',
            name='xiaji',
            field=models.BooleanField(default=False, verbose_name='\u4e0b\u673a'),
        ),
    ]
