# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-20 04:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calendar_app', '0020_auto_20170420_0043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='end_repeat',
            field=models.CharField(default='', max_length=200),
        ),
    ]
