# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-10-26 14:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cobranza', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='debe',
            name='glosa_debe',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='cobranza.RubroCobranza'),
        ),
    ]
