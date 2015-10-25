# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DBadmin', '0005_antecedentepretransplante_evento_pretransplante'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comuna',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('nombre', models.CharField(max_length=50)),
                ('region', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('nombre', models.CharField(max_length=100)),
                ('servicio_salud', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='paciente',
            name='sexo',
            field=models.CharField(null=True, max_length=1, choices=[('m', 'Masculino'), ('f', 'Femenino')]),
        ),
        migrations.AddField(
            model_name='paciente',
            name='comuna',
            field=models.ForeignKey(null=True, to='DBadmin.Comuna'),
        ),
        migrations.AddField(
            model_name='paciente',
            name='hospital',
            field=models.ForeignKey(null=True, to='DBadmin.Hospital'),
        ),
    ]
