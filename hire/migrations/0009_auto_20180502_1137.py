# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-05-02 06:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('hire', '0008_auto_20180501_1733'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='helpful',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='page',
            name='last_updated',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='page',
            name='unhelpful',
            field=models.IntegerField(default=0),
        ),
    ]