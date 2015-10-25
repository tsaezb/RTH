# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DBadmin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Antecedentes',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Enfermedad',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='paciente',
            name='direccion',
            field=models.CharField(null=True, max_length=200),
        ),
        migrations.AddField(
            model_name='paciente',
            name='grupo_sang',
            field=models.CharField(null=True, max_length=3, choices=[('o+', 'O Rh+'), ('a+', 'A Rh+'), ('b+', 'B Rh+'), ('ab+', 'AB Rh+'), ('o-', 'O Rh-'), ('a-', 'A Rh-'), ('b-', 'B Rh-'), ('ab-', 'AB Rh-')]),
        ),
        migrations.AddField(
            model_name='paciente',
            name='prevision',
            field=models.CharField(null=True, max_length=10, choices=[('fon', 'FONASA'), ('isa', 'ISAPRE')]),
        ),
        migrations.AddField(
            model_name='antecedentes',
            name='enfermedades_previas',
            field=models.ManyToManyField(to='DBadmin.Enfermedad'),
        ),
    ]
