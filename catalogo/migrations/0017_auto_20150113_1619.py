# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0016_auto_20141229_1412'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='materialesproductos',
            name='material',
        ),
        migrations.DeleteModel(
            name='Material',
        ),
        migrations.RemoveField(
            model_name='materialesproductos',
            name='producto',
        ),
        migrations.DeleteModel(
            name='MaterialesProductos',
        ),
    ]
