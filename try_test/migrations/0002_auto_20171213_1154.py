# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-12-13 02:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('try_test', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shorturl',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='shorturl',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='shorturl',
            name='shortcode',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]
