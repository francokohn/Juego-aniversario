# Generated by Django 3.2.6 on 2021-08-23 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('nickname', models.CharField(max_length=50)),
                ('correo', models.EmailField(max_length=254)),
                ('es_admin', models.BooleanField()),
                ('localidad', models.CharField(max_length=255)),
                ('ult_acceso', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'db_table': 'usuarios',
            },
        ),
    ]
