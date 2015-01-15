# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cmsloviz', '0008_auto_20150108_2043'),
    ]

    operations = [
        migrations.AddField(
            model_name='pagina',
            name='css',
            field=models.CharField(max_length=120, null=True, blank=True),
            preserve_default=True,
        ),
    ]
