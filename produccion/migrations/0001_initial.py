# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0016_auto_20141229_1412'),
    ]

    operations = [
        migrations.CreateModel(
            name='Planta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tipo', models.CharField(blank=True, max_length=100, null=True, choices=[(b'Mujer-001', b'Mujer-001'), (b'Hombre-002', b'Hombre-002')])),
                ('nombre', models.CharField(max_length=100, null=True, blank=True)),
                ('precio', models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True)),
                ('color', models.ForeignKey(blank=True, to='catalogo.Color', null=True)),
                ('talla', models.ForeignKey(blank=True, to='catalogo.Talla', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
