# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2019-01-07 03:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lab', '0008_auto_20181229_1628'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sample',
            name='library_type',
            field=models.CharField(blank=True, choices=[('scRNA_SCOPE', 'scRNA_SCOPE'), ('scRNA_10X', 'scRNA_10X'), ('RNA_Seq', 'RNA_Seq'), ('WES', 'WES'), ('Methylation', 'Methylation')], max_length=20),
        ),
    ]
