# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('DBadmin', '0004_auto_20151025_1927'),
    ]

    operations = [
        migrations.CreateModel(
            name='AntecedentePretransplante',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Antecedentes Pretransplante',
            },
        ),
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('tipo', models.CharField(max_length=100, choices=[('PreTX', 'PreTransplante'), ('TX', 'Transplante'), ('PostTX', 'PostTransplante')])),
                ('fecha', models.DateField(default=django.utils.timezone.now, verbose_name='Fecha del Evento')),
            ],
        ),
        migrations.CreateModel(
            name='Pretransplante',
            fields=[
                ('evento_ptr', models.OneToOneField(auto_created=True, serialize=False, primary_key=True, parent_link=True, to='DBadmin.Evento')),
                ('diagnostico', models.CharField(max_length=100)),
                ('causa_enlistamiento', models.CharField(max_length=100)),
                ('situacion', models.CharField(max_length=30, choices=[('Electivo', 'Electivo'), ('Urgencia1', 'Urgencia Tipo1'), ('Urgencia2', 'Urgencia Tipo2'), ('Urgencia3', 'Urgencia Tipo3')])),
                ('antecedentes_previos', models.ManyToManyField(to='DBadmin.AntecedentePretransplante')),
            ],
            bases=('DBadmin.evento',),
        ),
    ]
