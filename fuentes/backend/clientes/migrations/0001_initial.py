# Generated by Django 5.1 on 2024-08-08 09:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carrera',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, unique=True)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Fuente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, unique=True)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Institucion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, unique=True)),
                ('abreviatura', models.CharField(max_length=100, null=True)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('telefono', models.CharField(blank=True, max_length=10, null=True, unique=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True, unique=True)),
                ('genero', models.CharField(max_length=1)),
                ('ciclo', models.IntegerField(blank=True, null=True)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='')),
                ('carrera', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clientes.carrera')),
                ('fuente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clientes.fuente')),
                ('institucion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clientes.institucion')),
            ],
        ),
    ]