# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-03 11:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hire', '0003_auto_20180303_1706'),
    ]

    operations = [
        migrations.RenameField(
            model_name='service_category',
            old_name='name',
            new_name='namee',
        ),
    ]
