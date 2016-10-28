# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-10-28 06:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cobranza', '0005_cuotasocio'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cuotasocio',
            name='cuota',
        ),
        migrations.AddField(
            model_name='cuotasocio',
            name='cuota',
            field=models.ManyToManyField(to='cobranza.Cuota'),
        ),
    ]
