# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DBadmin', '0003_auto_20151025_1900'),
    ]

    operations = [
        migrations.CreateModel(
            name='Habito',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='antecedentes',
            name='enfermedades_previas',
        ),
        migrations.AddField(
            model_name='paciente',
            name='antecedentes_quirurgicos',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='paciente',
            name='enfermedades_previas',
            field=models.ManyToManyField(to='DBadmin.Enfermedad'),
        ),
        migrations.DeleteModel(
            name='Antecedentes',
        ),
        migrations.AddField(
            model_name='paciente',
            name='habitos',
            field=models.ManyToManyField(to='DBadmin.Habito'),
        ),
    ]
