# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-10-25 06:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socio', '0013_auto_20161025_0145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socio',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
