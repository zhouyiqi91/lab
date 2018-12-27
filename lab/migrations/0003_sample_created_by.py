# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-12-27 02:26
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('lab', '0002_auto_20181221_1304'),
    ]

    operations = [
        migrations.AddField(
            model_name='sample',
            name='created_by',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
