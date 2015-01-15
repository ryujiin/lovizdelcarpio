# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tienda.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ImagenesWeb',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=120)),
                ('imagen', models.ImageField(null=True, upload_to=tienda.models.url_imagen_pr, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
