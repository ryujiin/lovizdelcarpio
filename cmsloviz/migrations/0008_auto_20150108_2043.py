# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cmsloviz', '0007_link_peso'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='link',
            options={'ordering': ['peso']},
        ),
        migrations.AlterUniqueTogether(
            name='link',
            unique_together=set([('menu', 'peso')]),
        ),
    ]
