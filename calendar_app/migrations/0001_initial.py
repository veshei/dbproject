# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-12 06:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Calendar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calendar_name', models.CharField(max_length=200, unique=True)),
                ('color', models.CharField(default='blue', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='CalendarEvents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact', models.CharField(max_length=200)),
                ('calendar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='calendar_app.Calendar')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_title', models.CharField(max_length=200)),
                ('start_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('end_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('event_type', models.CharField(choices=[(0, 'general meeting'), (1, 'fundraiser'), (2, 'event'), (3, 'other')], max_length=1)),
                ('event_url', models.URLField()),
                ('location', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organization_name', models.CharField(max_length=200, unique=True)),
                ('email', models.EmailField(max_length=254)),
                ('website', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='RepeatingEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('frequency', models.CharField(choices=[(0, 'daily'), (1, 'weekly'), (2, 'monthly'), (3, 'yearly')], max_length=1)),
                ('day_of_week', models.CharField(choices=[(0, 'Sunday'), (1, 'Monday'), (2, 'Tuesday'), (3, 'Wednesday'), (4, 'Thursday'), (5, 'Friday'), (6, 'Saturday')], max_length=1)),
                ('end_repeat', models.DateTimeField()),
                ('event_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='calendar_app.Event')),
            ],
        ),
        migrations.AddField(
            model_name='calendarevents',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='calendar_app.Event'),
        ),
        migrations.AddField(
            model_name='calendarevents',
            name='organization',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='calendar_app.Organization'),
        ),
    ]