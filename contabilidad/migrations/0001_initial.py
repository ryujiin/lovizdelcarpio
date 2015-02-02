# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('material', '0001_initial'),
        ('catalogo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompraPlanta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('cantidad', models.PositiveIntegerField(default=1)),
                ('total', models.DecimalField(null=True, editable=False, max_digits=10, decimal_places=2, blank=True)),
                ('entregado', models.BooleanField(default=False)),
                ('en_stock', models.BooleanField(default=True)),
                ('planta', models.ForeignKey(blank=True, to='material.Planta', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Compras',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('precio', models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True)),
                ('material', models.ForeignKey(blank=True, to='material.Material', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='VentasMinorista',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cantidad', models.PositiveIntegerField(default=1)),
                ('producto', models.ForeignKey(blank=True, to='catalogo.Producto', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
