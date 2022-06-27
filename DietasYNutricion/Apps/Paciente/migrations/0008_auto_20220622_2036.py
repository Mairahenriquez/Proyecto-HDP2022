# Generated by Django 3.2.13 on 2022-06-22 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Paciente', '0007_auto_20220621_1450'),
    ]

    operations = [
        migrations.AlterField(
            model_name='departamento',
            name='name',
            field=models.CharField(max_length=40, unique=True),
        ),
        migrations.AlterField(
            model_name='municipio',
            name='name',
            field=models.CharField(max_length=40, unique=True),
        ),
        migrations.AlterField(
            model_name='planalimenticio',
            name='cantCarbohidratos',
            field=models.DecimalField(decimal_places=2, max_digits=4),
        ),
        migrations.AlterField(
            model_name='planalimenticio',
            name='cantGrasas',
            field=models.DecimalField(decimal_places=2, max_digits=4),
        ),
        migrations.AlterField(
            model_name='planalimenticio',
            name='cantMinerales',
            field=models.DecimalField(decimal_places=2, max_digits=4),
        ),
        migrations.AlterField(
            model_name='planalimenticio',
            name='cantProteina',
            field=models.DecimalField(decimal_places=2, max_digits=4),
        ),
        migrations.AlterField(
            model_name='planalimenticio',
            name='cantVitaminas',
            field=models.DecimalField(decimal_places=2, max_digits=4),
        ),
    ]