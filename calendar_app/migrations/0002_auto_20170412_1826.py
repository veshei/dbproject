# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-12 18:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calendar_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CalendarEvents',
            new_name='CalendarEvent',
        ),
        migrations.AlterField(
            model_name='event',
            name='start_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
