# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-12-16 03:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lab', '0010_auto_20181216_1100'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sample',
            old_name='aati',
            new_name='AATI',
        ),
    ]