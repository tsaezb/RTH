# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-26 21:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('DBadmin', '0013_auto_20151027_0235'),
    ]

    operations = [
        migrations.CreateModel(
            name='Donante',
            fields=[
                ('evento_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='DBadmin.Evento')),
                ('nombre', models.CharField(max_length=200)),
                ('rut', models.CharField(max_length=10)),
                ('sexo', models.CharField(choices=[('m', 'Masculino'), ('f', 'Femenino')], max_length=1, null=True)),
                ('edad', models.IntegerField(default=0)),
                ('peso', models.IntegerField(default=0)),
                ('talla', models.IntegerField(default=0)),
                ('grupo_sang', models.CharField(choices=[('o+', 'O Rh+'), ('a+', 'A Rh+'), ('b+', 'B Rh+'), ('ab+', 'AB Rh+'), ('o-', 'O Rh-'), ('a-', 'A Rh-'), ('b-', 'B Rh-'), ('ab-', 'AB Rh-')], max_length=3, null=True)),
                ('tipo_injerto', models.CharField(choices=[('injerto1', 'Injerto 1'), ('injerto2', 'Injerto 2'), ('injerto3', 'Injerto 3')], max_length=3)),
                ('bar_score', models.FloatField(default=0)),
                ('vivo_muerto', models.NullBooleanField()),
                ('hospital', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='DBadmin.Hospital')),
            ],
            bases=('DBadmin.evento',),
        ),
        migrations.CreateModel(
            name='Laboratorio',
            fields=[
                ('evento_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='DBadmin.Evento')),
                ('fecha_lab', models.DateField(default=django.utils.timezone.now)),
                ('got', models.FloatField(default=0)),
                ('gpt', models.FloatField(default=0)),
                ('fa', models.FloatField(default=0)),
                ('ggt', models.FloatField(default=0)),
                ('bilis_total', models.FloatField(default=0)),
                ('bilis_dir', models.FloatField(default=0)),
                ('inr', models.FloatField(default=0)),
            ],
            bases=('DBadmin.evento',),
        ),
        migrations.CreateModel(
            name='Rehospitalizacion',
            fields=[
                ('evento_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='DBadmin.Evento')),
                ('fecha_rehospitalizacion', models.DateField(default=django.utils.timezone.now)),
                ('causa_rehospitalizacion', models.TextField(default='', max_length=500)),
            ],
            bases=('DBadmin.evento',),
        ),
        migrations.CreateModel(
            name='Trasplante',
            fields=[
                ('evento_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='DBadmin.Evento')),
                ('fecha_operacion', models.DateField(default=django.utils.timezone.now)),
                ('score_child', models.FloatField(default=0)),
                ('factor_de_reajuste_childpugh', models.FloatField(default=0)),
                ('score_meld', models.FloatField(default=0)),
                ('situacion', models.CharField(choices=[('Electivo', 'Electivo'), ('Urgencia1', 'Urgencia Tipo1'), ('Urgencia2', 'Urgencia Tipo2'), ('Urgencia3', 'Urgencia Tipo3')], max_length=30)),
                ('tipo_solucion', models.CharField(choices=[('solucion1', 'Solucion 1'), ('solucion2', 'Solucion 2'), ('solucion3', 'Solucion 3')], max_length=30)),
                ('distribucion_solucion', models.CharField(choices=[('solucion1', 'Solucion 1'), ('solucion2', 'Solucion 2'), ('solucion3', 'Solucion 3')], max_length=30)),
                ('porcentaje_esteatosis', models.FloatField(default=0)),
                ('tiempo_total', models.IntegerField(default=0)),
                ('izquemia_fria', models.IntegerField(default=0)),
                ('izquemia_caliente', models.IntegerField(default=0)),
                ('tecnica', models.CharField(choices=[('tecnica1', 'Tecnica 1'), ('tecnica2', 'Tecnica 2'), ('tecnica3', 'Tecnica 3')], max_length=30)),
            ],
            bases=('DBadmin.evento',),
        ),
        migrations.RenameModel(
            old_name='AntecedentePretransplante',
            new_name='AntecedentePretrasplante',
        ),
        migrations.RenameModel(
            old_name='Pretransplante',
            new_name='Pretrasplante',
        ),
        migrations.AlterModelOptions(
            name='antecedentepretrasplante',
            options={'verbose_name_plural': 'Antecedentes Pretrasplante'},
        ),
        migrations.AddField(
            model_name='complicacion',
            name='operacion',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='evento',
            name='tipo',
            field=models.CharField(choices=[('PreTX', 'PreTrasplante'), ('TX', 'Trasplante'), ('PostTX', 'PostOperatorio'), ('Compl', 'Complicacion'), ('ReHos', 'Rehospitalizacion'), ('Lab', 'Laboratorio'), ('Don', 'Donante')], max_length=100),
        ),
    ]
