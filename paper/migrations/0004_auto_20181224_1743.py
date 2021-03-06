# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-12-24 09:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paper', '0003_auto_20181224_1741'),
    ]

    operations = [
        migrations.AddField(
            model_name='paper',
            name='submit1_already',
            field=models.BooleanField(default=False, editable=False, verbose_name='submite1'),
        ),
        migrations.AddField(
            model_name='paper',
            name='submit2_already',
            field=models.BooleanField(default=False, editable=False, verbose_name='submit2'),
        ),
        migrations.AlterField(
            model_name='paper',
            name='submit1',
            field=models.FileField(upload_to='SGRNJ/Database/test/1.11/lab_project/media/paper/submit'),
        ),
        migrations.AlterField(
            model_name='paper',
            name='submit2',
            field=models.FileField(upload_to='SGRNJ/Database/test/1.11/lab_project/media/paper/submit'),
        ),
    ]
