# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-12-19 06:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lab', '0029_remove_sample_people'),
    ]

    operations = [
        migrations.AddField(
            model_name='sample',
            name='library_type',
            field=models.CharField(choices=[('scope', 'scRNA-SCOPE'), ('X10', 'scRNA-10X'), ('RNA', 'RNA-Seq'), ('WES', 'WES')], default='scope', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sample',
            name='species',
            field=models.CharField(choices=[('human', 'hm'), ('mouse', 'mm'), ('human_mouse', 'hm_mm'), ('other', 'other')], default='hm', max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='employee',
            name='department',
            field=models.CharField(choices=[('lab', '\u5b9e\u9a8c'), ('bioinfo', '\u751f\u4fe1'), ('administration', '\u884c\u653f')], max_length=30, verbose_name='\u90e8\u95e8'),
        ),
    ]