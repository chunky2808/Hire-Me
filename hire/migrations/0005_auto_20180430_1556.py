# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-30 15:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hire', '0004_auto_20180430_1552'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service_category',
            name='downvotes',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='service_category',
            name='upvotes',
            field=models.IntegerField(default=0),
        ),
    ]
