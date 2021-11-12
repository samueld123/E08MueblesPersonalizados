# Generated by Django 3.2.9 on 2021-11-11 02:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ventas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Sell', models.DateField(max_length=200, verbose_name='Fecha venta')),
                ('city', models.CharField(max_length=200, verbose_name='Ciudad')),
            ],
            options={
                'verbose_name': 'Venta',
                'verbose_name_plural': 'Ventas',
            },
        ),
    ]
