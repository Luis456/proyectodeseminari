# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_auto_20141008_1744'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='perfil',
            options={'permissions': (('ver_perfil', 'permite ver el perfil'), ('cambiar_perfil', 'permite modificar el perfil'))},
        ),
    ]
