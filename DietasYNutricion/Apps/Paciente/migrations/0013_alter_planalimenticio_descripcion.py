# Generated by Django 3.2.13 on 2022-06-23 19:39

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Paciente', '0012_auto_20220622_2101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='planalimenticio',
            name='descripcion',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
