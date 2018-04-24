# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-21 18:55
from __future__ import unicode_literals

from django.db import migrations
import geoposition.fields


class Migration(migrations.Migration):

    dependencies = [
        ('hire', '0013_auto_20180421_1819'),
    ]

    operations = [
        migrations.AddField(
            model_name='service_category',
            name='position',
            field=geoposition.fields.GeopositionField(max_length=42, null=True),
        ),
    ]