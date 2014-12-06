# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='respuesta',
            name='respusta_opciona2',
            field=models.CharField(default=1, max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='respuesta',
            name='respusta_opciona3',
            field=models.CharField(default=1, max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='respuesta',
            name='respusta_opciona4',
            field=models.CharField(default=1, max_length=500),
            preserve_default=False,
        ),
    ]
