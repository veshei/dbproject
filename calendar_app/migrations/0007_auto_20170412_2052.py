# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-12 20:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('calendar_app', '0006_auto_20170412_2017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='start_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]