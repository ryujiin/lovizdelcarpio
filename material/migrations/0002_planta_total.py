# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('material', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='planta',
            name='total',
            field=models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True),
            preserve_default=True,
        ),
    ]
