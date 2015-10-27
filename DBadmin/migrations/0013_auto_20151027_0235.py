# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('DBadmin', '0012_auto_20151026_1820'),
    ]

    operations = [
        migrations.CreateModel(
            name='Complicacion',
            fields=[
                ('evento_ptr', models.OneToOneField(serialize=False, parent_link=True, to='DBadmin.Evento', primary_key=True, auto_created=True)),
                ('tipo_complicacion', models.CharField(max_length=4, choices=[('rech', 'Rechazo'), ('vasc', 'Vascular'), ('bili', 'Biliar'), ('infe', 'Infeccion'), ('neur', 'Neurologica'), ('neop', 'Neoplasica'), ('card', 'Cardiovascular'), ('enfb', 'Reaparicion enfermedad base')])),
                ('fecha_complicacion', models.DateField(default=django.utils.timezone.now)),
                ('tratamiento', models.TextField(default='', max_length=500)),
                ('detalles', models.TextField(default='', max_length=500)),
            ],
            bases=('DBadmin.evento',),
        ),
        migrations.AlterField(
            model_name='evento',
            name='tipo',
            field=models.CharField(max_length=100, choices=[('PreTX', 'PreTransplante'), ('TX', 'Transplante'), ('PostTX', 'PostOperatorio'), ('Compl', 'Complicacion')]),
        ),
    ]
