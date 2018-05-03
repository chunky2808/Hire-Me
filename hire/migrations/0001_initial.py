# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-05-03 19:30
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import geoposition.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Review', models.TextField(max_length=4000)),
                ('last_updated', models.DateTimeField(auto_now_add=True)),
                ('helpful', models.IntegerField(default=0)),
                ('unhelpful', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Service_category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('namee', models.CharField(max_length=100, unique=True)),
                ('desc', models.CharField(max_length=150)),
                ('price', models.CharField(max_length=10)),
                ('Address', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=50)),
                ('last_updated', models.DateTimeField(auto_now_add=True)),
                ('position', geoposition.fields.GeopositionField(max_length=42, null=True)),
                ('upvotes', models.IntegerField(default=0)),
                ('downvotes', models.IntegerField(default=0)),
                ('distance', models.DecimalField(decimal_places=3, default=0.0, max_digits=25)),
            ],
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, unique=True)),
                ('category', models.CharField(max_length=40)),
                ('last_updated', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='service_category',
            name='service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='serces', to='hire.Services'),
        ),
        migrations.AddField(
            model_name='page',
            name='service_cat',
            field=models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, related_name='ser_cat', to='hire.Service_category'),
        ),
        migrations.AddField(
            model_name='page',
            name='service_main',
            field=models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, related_name='ser_main', to='hire.Services'),
        ),
        migrations.AddField(
            model_name='page',
            name='started_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
