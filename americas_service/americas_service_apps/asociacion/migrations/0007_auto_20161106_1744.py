# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-11-06 22:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asociacion', '0006_auto_20161106_1740'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Banco',
        ),
        migrations.DeleteModel(
            name='TipoCuenta',
        ),
        migrations.RemoveField(
            model_name='informacionlote',
            name='lote',
        ),
        migrations.AddField(
            model_name='lote',
            name='area_lote',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5, verbose_name='area total'),
        ),
    ]