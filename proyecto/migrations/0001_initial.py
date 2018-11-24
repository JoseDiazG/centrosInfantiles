# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2018-11-23 17:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Centro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Centro_Servicios',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('centro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proyecto.Centro')),
            ],
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('periodo', models.DateField()),
                ('centro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proyecto.Centro')),
            ],
        ),
        migrations.CreateModel(
            name='Detalle_Representante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Docente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Localidad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('provincia', models.CharField(max_length=45)),
                ('canton', models.CharField(max_length=45)),
                ('parroquia', models.CharField(max_length=45)),
                ('latitud', models.CharField(max_length=45)),
                ('longitud', models.CharField(max_length=45)),
                ('direccion', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Nino',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cedula', models.IntegerField()),
                ('nombres', models.CharField(max_length=40)),
                ('apellidos', models.CharField(max_length=40)),
                ('edad', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cedula', models.IntegerField()),
                ('nombres', models.CharField(max_length=40)),
                ('apellidos', models.CharField(max_length=40)),
                ('direccion', models.CharField(max_length=40)),
                ('telefono', models.IntegerField()),
                ('email', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Representante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cant_hijos', models.IntegerField()),
                ('persona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proyecto.Persona')),
            ],
        ),
        migrations.CreateModel(
            name='Sala',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_sala', models.IntegerField()),
                ('capacidad', models.IntegerField()),
                ('descripcion', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Servicios',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=45)),
                ('detalle', models.CharField(max_length=45)),
            ],
        ),
        migrations.AddField(
            model_name='localidad',
            name='servicios',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proyecto.Servicios'),
        ),
        migrations.AddField(
            model_name='docente',
            name='persona',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proyecto.Persona'),
        ),
        migrations.AddField(
            model_name='detalle_representante',
            name='nino',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proyecto.Nino'),
        ),
        migrations.AddField(
            model_name='detalle_representante',
            name='representante',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proyecto.Representante'),
        ),
        migrations.AddField(
            model_name='curso',
            name='docente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proyecto.Docente'),
        ),
        migrations.AddField(
            model_name='curso',
            name='sala',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proyecto.Sala'),
        ),
        migrations.AddField(
            model_name='centro_servicios',
            name='servicios',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proyecto.Servicios'),
        ),
        migrations.AddField(
            model_name='alumno',
            name='curso',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proyecto.Curso'),
        ),
        migrations.AddField(
            model_name='alumno',
            name='nino',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proyecto.Nino'),
        ),
    ]