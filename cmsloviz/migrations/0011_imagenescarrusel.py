# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import cmsloviz.models


class Migration(migrations.Migration):

    dependencies = [
        ('cmsloviz', '0010_auto_20150112_1331'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImagenesCarrusel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('imagen', models.ImageField(null=True, upload_to=cmsloviz.models.url_imagen_carrusel, blank=True)),
                ('titulo', models.CharField(max_length=130, null=True, blank=True)),
                ('order', models.PositiveIntegerField(default=1)),
                ('carrusel', models.ForeignKey(related_name='imagenes_carrusel', blank=True, to='cmsloviz.Carrusel', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
