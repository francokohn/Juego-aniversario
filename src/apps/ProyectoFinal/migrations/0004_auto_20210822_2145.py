# Generated by Django 3.2.6 on 2021-08-22 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProyectoFinal', '0003_auto_20210821_1448'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='correo',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='es_admin',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='localidad',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='nickname',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='nombre',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]