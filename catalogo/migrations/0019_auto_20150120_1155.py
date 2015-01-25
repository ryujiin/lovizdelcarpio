# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0018_auto_20150120_1142'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='genero',
            name='imagen',
        ),
        migrations.AddField(
            model_name='genero',
            name='foto',
            field=models.ImageField(null=True, upload_to=b'genero/fotos/', blank=True),
            preserve_default=True,
        ),
    ]
