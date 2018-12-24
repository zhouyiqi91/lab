# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-12-24 09:41
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paper', '0002_auto_20181224_1728'),
    ]

    operations = [
        migrations.AddField(
            model_name='paper',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='paper',
            name='paper_people',
            field=models.ManyToManyField(related_name='paper_peoples', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='paper',
            name='submit1',
            field=models.BooleanField(default=False, editable=False),
        ),
        migrations.AlterField(
            model_name='paper',
            name='submit2',
            field=models.BooleanField(default=False, editable=False),
        ),
    ]