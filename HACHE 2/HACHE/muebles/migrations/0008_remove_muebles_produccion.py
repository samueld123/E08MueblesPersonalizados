# Generated by Django 3.2.9 on 2021-11-12 02:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('muebles', '0007_muebles_produccion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='muebles',
            name='produccion',
        ),
    ]
