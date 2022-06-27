# Generated by Django 3.2.13 on 2022-06-27 00:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Paciente', '0020_alter_paciente_peso'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='dui',
            field=models.CharField(max_length=9, unique=True),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='peso',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]