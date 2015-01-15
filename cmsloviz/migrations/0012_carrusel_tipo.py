# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cmsloviz', '0011_imagenescarrusel'),
    ]

    operations = [
        migrations.AddField(
            model_name='carrusel',
            name='tipo',
            field=models.CharField(blank=True, max_length=100, null=True, choices=[(b'modelo', b'model'), (b'imagenes', b'imagenes')]),
            preserve_default=True,
        ),
    ]
