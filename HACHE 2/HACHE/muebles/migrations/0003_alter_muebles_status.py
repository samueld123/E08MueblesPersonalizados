# Generated by Django 3.2.9 on 2021-11-11 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('muebles', '0002_alter_muebles_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='muebles',
            name='status',
            field=models.CharField(choices=[('Nuevo', 'Nuevo'), ('En producciónP', 'En producción'), ('Entregado', 'Entregado')], max_length=200, verbose_name='Estado'),
        ),
    ]
