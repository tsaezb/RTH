# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DBadmin', '0011_auto_20151026_1220'),
    ]

    operations = [
        migrations.CreateModel(
            name='Postoperatorio',
            fields=[
                ('evento_ptr', models.OneToOneField(serialize=False, parent_link=True, to='DBadmin.Evento', primary_key=True, auto_created=True)),
                ('dias_totales', models.IntegerField(default=0)),
                ('dias_uci', models.IntegerField(default=0)),
                ('horas_ventilacion_mecanica', models.IntegerField(default=0)),
                ('dias_soporte_renal', models.IntegerField(default=0)),
                ('hcc', models.NullBooleanField()),
                ('peso', models.FloatField(default=0)),
                ('datos_interes', models.TextField(max_length=500, default='')),
            ],
            bases=('DBadmin.evento',),
        ),
        migrations.AlterField(
            model_name='evento',
            name='tipo',
            field=models.CharField(max_length=100, choices=[('PreTX', 'PreTransplante'), ('TX', 'Transplante'), ('PostTX', 'PostOperatorio')]),
        ),
    ]
