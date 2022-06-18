# Generated by Django 3.2.13 on 2022-06-16 01:01

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Usuario', '0004_rename_gestionarusuario_usuario'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='usuario',
            options={'verbose_name': 'usuario', 'verbose_name_plural': 'usuarios'},
        ),
        migrations.AddField(
            model_name='usuario',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2022, 6, 16, 1, 0, 56, 744577, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usuario',
            name='update',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2022, 6, 16, 1, 1, 9, 29523, tzinfo=utc)),
            preserve_default=False,
        ),
    ]