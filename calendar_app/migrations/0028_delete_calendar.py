# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-20 05:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calendar_app', '0027_auto_20170420_0105'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Calendar',
        ),
    ]