# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-05 18:40
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hire', '0007_service_category_last_updated'),
    ]

    operations = [
        migrations.CreateModel(
            name='xyz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Review', models.TextField(max_length=4000)),
                ('started_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='service_category',
            name='price',
            field=models.CharField(max_length=10),
        ),
    ]
