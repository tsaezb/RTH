# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DBadmin', '0006_auto_20151025_2012'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='hospital',
            options={'verbose_name_plural': 'Hospitales'},
        ),
    ]
