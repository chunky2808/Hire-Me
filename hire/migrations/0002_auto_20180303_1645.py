# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-03 11:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hire', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='services',
            name='category',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='services',
            name='name',
            field=models.CharField(max_length=40),
        ),
    ]
