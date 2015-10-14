# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=200)),
                ('rut', models.CharField(max_length=10)),
                ('sexo', models.CharField(max_length=1)),
                ('fecha_nac', models.DateField(verbose_name='Fecha de Nacimiento')),
            ],
        ),
    ]
