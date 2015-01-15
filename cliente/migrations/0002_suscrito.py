# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Suscrito',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.CharField(max_length=100, null=True, blank=True)),
                ('suscrito', models.BooleanField(default=True)),
                ('usuario', models.BooleanField(default=True)),
                ('cliente', models.ForeignKey(blank=True, to='cliente.Cliente', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
