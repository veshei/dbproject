# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-20 04:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calendar_app', '0022_remove_event_end_repeat'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='end_repeat',
            field=models.CharField(default='', max_length=200),
        ),
    ]
