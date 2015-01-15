# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cmsloviz', '0009_pagina_css'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bloque',
            name='pagina',
        ),
        migrations.RemoveField(
            model_name='bloque',
            name='pagina_excluir',
        ),
        migrations.RemoveField(
            model_name='carrusel',
            name='pagina',
        ),
        migrations.AddField(
            model_name='bloque',
            name='paginas_mostrar',
            field=models.ManyToManyField(related_name='bloques', null=True, to='cmsloviz.Pagina', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='bloque',
            name='paginas_no_mostrar',
            field=models.ManyToManyField(related_name='bloques_excluidos', null=True, to='cmsloviz.Pagina', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='carrusel',
            name='paginas_mostrar',
            field=models.ManyToManyField(related_name='carrusel', null=True, to='cmsloviz.Pagina', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='carrusel',
            name='paginas_no_mostrar',
            field=models.ManyToManyField(related_name='carrusel_excluido', null=True, to='cmsloviz.Pagina', blank=True),
            preserve_default=True,
        ),
    ]
