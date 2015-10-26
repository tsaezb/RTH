# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('DBadmin', '0010_auto_20151025_2233'),
    ]

    operations = [
        migrations.AddField(
            model_name='evento',
            name='paciente',
            field=models.ForeignKey(null=True, to='DBadmin.Paciente'),
        ),
        migrations.AddField(
            model_name='pretransplante',
            name='estatura',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='pretransplante',
            name='factor_de_reajuste_childpugh',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='pretransplante',
            name='fecha_enlistamiento',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='pretransplante',
            name='peso',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='pretransplante',
            name='score_child',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='pretransplante',
            name='score_meld',
            field=models.FloatField(default=0),
        ),
    ]
