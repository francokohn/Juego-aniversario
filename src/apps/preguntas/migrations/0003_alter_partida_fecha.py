# Generated by Django 3.2.6 on 2021-08-29 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('preguntas', '0002_partida_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partida',
            name='fecha',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
