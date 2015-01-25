# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0017_auto_20150113_1619'),
    ]

    operations = [
        migrations.AddField(
            model_name='genero',
            name='descripcion',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='genero',
            name='imagen',
            field=models.ImageField(default='ad', upload_to=b'/genero/'),
            preserve_default=False,
        ),
    ]
