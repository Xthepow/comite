# Generated by Django 5.1.1 on 2024-09-12 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comite', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingresos',
            name='nIngreso',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]