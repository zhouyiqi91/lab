# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-12-19 06:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lab', '0030_auto_20181219_1423'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sample',
            name='library_type',
            field=models.CharField(blank=True, choices=[('scope', 'scRNA-SCOPE'), ('X10', 'scRNA-10X'), ('RNA', 'RNA-Seq'), ('WES', 'WES')], max_length=20),
        ),
    ]
