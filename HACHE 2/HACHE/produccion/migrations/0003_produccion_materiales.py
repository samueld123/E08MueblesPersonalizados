# Generated by Django 3.2.9 on 2021-11-12 02:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('material', '0001_initial'),
        ('produccion', '0002_produccion_muebles'),
    ]

    operations = [
        migrations.AddField(
            model_name='produccion',
            name='materiales',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='material.materiales'),
        ),
    ]