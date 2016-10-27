# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-10-27 02:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ConceptoCobranza',
            fields=[
                ('concepto_id', models.AutoField(primary_key=True, serialize=False)),
                ('concepto_cobranza', models.CharField(max_length=80, unique=True)),
                ('estado', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'ConceptoCobranza',
                'verbose_name_plural': 'ConceptoCobranzas',
            },
        ),
        migrations.CreateModel(
            name='Debe',
            fields=[
                ('codigo_deb', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name': 'Debe',
                'verbose_name_plural': 'Debes',
            },
        ),
        migrations.CreateModel(
            name='Mora',
            fields=[
                ('mora_id', models.AutoField(primary_key=True, serialize=False)),
                ('concepto_mora', models.CharField(max_length=100, unique=True)),
                ('detalle_mora', models.TextField(blank=True, max_length=300, null=True)),
                ('valor', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=5, null=True)),
                ('estado', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Mora',
                'verbose_name_plural': 'Moras',
            },
        ),
        migrations.CreateModel(
            name='RubroCobranza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rubro_cobranza', models.CharField(max_length=100, unique=True)),
                ('importe', models.DecimalField(decimal_places=2, max_digits=5)),
                ('con_mora', models.CharField(choices=[('Si', 'Si'), ('No', 'No')], max_length=2)),
                ('mora', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=5, null=True)),
                ('detalle', models.TextField(blank=True, max_length=500, null=True)),
                ('fecha_inicio', models.DateField()),
                ('fecha_fin', models.DateField()),
                ('concepto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cobranza.ConceptoCobranza')),
            ],
            options={
                'verbose_name': 'RubroCobranza',
                'verbose_name_plural': 'RubroCobranzas',
            },
        ),
        migrations.AddField(
            model_name='debe',
            name='glosa_debe',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='cobranza.RubroCobranza'),
        ),
    ]
