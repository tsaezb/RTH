# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DBadmin', '0008_auto_20151025_2231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='antecedentes_quirurgicos',
            field=models.BooleanField(default='No'),
        ),
    ]
