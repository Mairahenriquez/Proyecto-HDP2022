# Generated by Django 3.2.13 on 2022-06-22 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Paciente', '0009_alter_departamento_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='departamento',
            name='name',
            field=models.CharField(max_length=40, unique=True),
        ),
    ]
