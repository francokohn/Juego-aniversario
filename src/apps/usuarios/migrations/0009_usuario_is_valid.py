# Generated by Django 3.2.6 on 2021-08-26 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0008_remove_usuario_es_admin'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='is_valid',
            field=models.BooleanField(default=True),
        ),
    ]
