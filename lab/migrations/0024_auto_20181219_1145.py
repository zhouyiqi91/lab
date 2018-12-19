# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-12-19 03:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lab', '0023_auto_20181219_1138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='bioinfo_staff',
            field=models.ManyToManyField(to='lab.Bioinfo_staff'),
        ),
        migrations.AlterField(
            model_name='project',
            name='lab_staff',
            field=models.ManyToManyField(to='lab.Lab_staff'),
        ),
        migrations.AlterField(
            model_name='sample',
            name='bioinfo_staff',
            field=models.ManyToManyField(to='lab.Bioinfo_staff'),
        ),
        migrations.AlterField(
            model_name='sample',
            name='lab_staff',
            field=models.ManyToManyField(to='lab.Lab_staff'),
        ),
    ]
