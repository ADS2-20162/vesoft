# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-01 03:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('asociacion', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=300)),
                ('detalle', models.TextField(max_length=600)),
                ('importe_total', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('estado', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
            },
        ),
        migrations.CreateModel(
            name='ConceptoCobranza',
            fields=[
                ('concepto_id', models.AutoField(primary_key=True, serialize=False)),
                ('concepto_cobranza', models.CharField(max_length=80, unique=True)),
                ('estado', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Concepto de cobranza',
                'verbose_name_plural': 'Conceptos de cobranzas',
            },
        ),
        migrations.CreateModel(
            name='Cuota',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cuota', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('lote', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='asociacion.Lote')),
            ],
            options={
                'verbose_name': 'Cuota',
                'verbose_name_plural': 'Cuotas',
            },
        ),
        migrations.CreateModel(
            name='CuotaSocio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cuota', models.ManyToManyField(to='cobranza.Cuota')),
                ('socio', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='asociacion.SocioLote')),
            ],
            options={
                'verbose_name': 'CuotaSocio',
                'verbose_name_plural': 'CuotaSocios',
            },
        ),
        migrations.CreateModel(
            name='RubroCobranza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rubro_cobranza', models.CharField(max_length=100, unique=True)),
                ('importe', models.DecimalField(decimal_places=2, max_digits=5)),
                ('con_mora', models.BooleanField(default=False)),
                ('mora', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=5, null=True)),
                ('detalle', models.TextField(blank=True, max_length=500, null=True)),
                ('fecha_inicio', models.DateField()),
                ('dias', models.IntegerField()),
                ('concepto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cobranza.ConceptoCobranza')),
            ],
            options={
                'verbose_name': 'Rubro de cobranza',
                'verbose_name_plural': 'Rubros de cobranza',
            },
        ),
        migrations.AddField(
            model_name='cuota',
            name='rubro_cobranza',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cobranza.RubroCobranza'),
        ),
    ]
