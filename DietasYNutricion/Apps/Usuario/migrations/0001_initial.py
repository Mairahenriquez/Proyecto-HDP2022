# Generated by Django 3.2.13 on 2022-06-15 02:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GUsuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Nombre de usuario')),
                ('email', models.EmailField(max_length=50, unique=True, verbose_name='Correo Electrónico')),
                ('password', models.CharField(max_length=50, unique=True, verbose_name='Password')),
                ('rol', models.CharField(max_length=50, unique=True, verbose_name='Rol')),
            ],
        ),
        migrations.CreateModel(
            name='MUsuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Nombre de usuario')),
                ('email', models.EmailField(max_length=50, unique=True, verbose_name='Correo Electrónico')),
                ('password', models.CharField(max_length=50, unique=True, verbose_name='Password')),
                ('rol', models.CharField(max_length=50, unique=True, verbose_name='Rol')),
            ],
        ),
    ]