# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-20 04:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calendar_app', '0021_auto_20170420_0044'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='end_repeat',
        ),
    ]
