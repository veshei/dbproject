# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-20 04:58
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('calendar_app', '0025_auto_20170420_0054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='end_repeat',
            field=models.DateTimeField(default=datetime.datetime(2017, 4, 20, 4, 58, 31, 837818, tzinfo=utc)),
        ),
    ]