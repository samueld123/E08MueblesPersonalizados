# Generated by Django 3.2.9 on 2021-11-11 01:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='clientes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Nombre')),
                ('docu', models.CharField(choices=[('CC', 'Cédula de ciudadanía'), ('CE', 'Cédula de extrangería'), ('TI', 'Tarjeta de identidad'), ('NTI', 'NIT'), ('PAS', 'Pasaporte')], max_length=200, verbose_name='Tipo de documento')),
                ('number_docu', models.CharField(max_length=200, verbose_name='Número de documento')),
                ('email', models.CharField(max_length=200, verbose_name='Correo electónico')),
                ('phone', models.CharField(max_length=200, verbose_name='Telefono')),
                ('address', models.CharField(max_length=200, verbose_name='Dirección')),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
            },
        ),
    ]