# Generated by Django 5.1.1 on 2024-11-21 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comite', '0037_ingresos_facturas'),
    ]

    operations = [
        migrations.AddField(
            model_name='facturar',
            name='valor_pagado',
            field=models.IntegerField(default=0),
        ),
    ]