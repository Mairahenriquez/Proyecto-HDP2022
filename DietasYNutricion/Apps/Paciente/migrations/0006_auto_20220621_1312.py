# Generated by Django 3.2.13 on 2022-06-21 13:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Paciente', '0005_auto_20220621_0243'),
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
