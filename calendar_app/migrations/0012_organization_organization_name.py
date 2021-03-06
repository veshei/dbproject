# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-18 22:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calendar_app', '0011_auto_20170418_1835'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='organization_name',
            field=models.CharField(choices=[('aKDPHI', 'alpha Kappa Delta Phi'), ('ASU', 'Asian Student Union'), ('BKD', 'Barkada'), ('BCT', 'Beta Chi Theta'), ('DPO', 'Delta Phi Omega'), ('KASA', 'Korean American Student Organization'), ('KPL', 'Kappa Phi Lambda'), ('PDP', 'Pi Delta Psi'), ('SASE', 'Society of Asian Scientists and Engineers'), ('UTSAV', 'UTSAV'), ('VSA', 'Vietnamese Student Association')], default='', max_length=200),
        ),
    ]
