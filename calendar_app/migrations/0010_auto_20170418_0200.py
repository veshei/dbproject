# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-18 06:00
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('calendar_app', '0009_auto_20170417_1800'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserOrganization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AlterField(
            model_name='organization',
            name='organization_name',
            field=models.CharField(choices=[('aKDPHI', 'alpha Kappa Delta Phi'), ('ASU', 'Asian Student Union'), ('BKD', 'Barkada'), ('BCT', 'Beta Chi Theta'), ('DPO', 'Delta Phi Omega'), ('KASA', 'Korean American Student Organization'), ('KPL', 'Kappa Phi Lambda'), ('PDP', 'Pi Delta Psi'), ('SASE', 'Society of Asian Scientists and Engineers'), ('UTSAV', 'UTSAV'), ('VSA', 'Vietnamese Student Association')], max_length=200),
        ),
        migrations.AddField(
            model_name='userorganization',
            name='organization',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='calendar_app.Organization'),
        ),
        migrations.AddField(
            model_name='userorganization',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
