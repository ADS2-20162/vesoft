# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-11-04 04:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('asociacion', '0002_auto_20161103_2331'),
    ]

    operations = [
        migrations.RenameField(
            model_name='informacionlote',
            old_name='informacion_lote',
            new_name='lote',
        ),
    ]