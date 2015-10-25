# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DBadmin', '0002_auto_20151025_1844'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='antecedentes',
            options={'verbose_name_plural': 'Antecedentes'},
        ),
        migrations.AlterModelOptions(
            name='enfermedad',
            options={'verbose_name_plural': 'Enfermedades'},
        ),
    ]
