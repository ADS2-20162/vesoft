# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-11-04 06:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('asociacion', '0003_auto_20161103_2350'),
        ('cobranza', '0003_auto_20161104_0108'),
        ('pagos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ValidarPago',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('importe_deposito', models.DecimalField(decimal_places=2, max_digits=5)),
                ('fecha_deposito', models.DateField()),
                ('numero_operacion', models.CharField(max_length=50)),
                ('imagen_voucher', models.ImageField(blank=True, upload_to='')),
                ('cuenta_banco', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='asociacion.CuentaBanco')),
                ('cuota_socio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cobranza.CuotaSocio')),
            ],
            options={
                'verbose_name_plural': 'ValidarPagos',
                'verbose_name': 'ValidarPago',
            },
        ),
    ]