# Generated by Django 3.2.13 on 2022-06-15 21:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Usuario', '0002_rename_musuario_rusuario'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='RUsuario',
            new_name='GestionarUsuario',
        ),
        migrations.DeleteModel(
            name='GUsuario',
        ),
    ]
