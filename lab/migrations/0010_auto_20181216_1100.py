# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-12-16 03:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lab', '0009_sample_imagefield'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sample',
            old_name='ImageField',
            new_name='aati',
        ),
        migrations.AlterField(
            model_name='sample',
            name='report',
            field=models.FilePathField(),
        ),
    ]
