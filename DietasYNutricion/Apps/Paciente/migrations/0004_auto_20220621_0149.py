# Generated by Django 3.2.13 on 2022-06-21 01:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Paciente', '0003_auto_20220620_0246'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Country',
            new_name='Departamento',
        ),
        migrations.RenameModel(
            old_name='City',
            new_name='Municipio',
        ),
        migrations.RenameField(
            model_name='municipio',
            old_name='country',
            new_name='departamento',
        ),
        migrations.RenameField(
            model_name='paciente',
            old_name='country',
            new_name='departamento',
        ),
        migrations.RenameField(
            model_name='paciente',
            old_name='city',
            new_name='municipio',
        ),
    ]
