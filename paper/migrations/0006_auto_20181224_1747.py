# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-12-24 09:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paper', '0005_auto_20181224_1745'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paper',
            name='submit1_already',
            field=models.BooleanField(default=False, editable=False, verbose_name='submit_1'),
        ),
        migrations.AlterField(
            model_name='paper',
            name='submit2_already',
            field=models.BooleanField(default=False, editable=False, verbose_name='submit_2'),
        ),
    ]
