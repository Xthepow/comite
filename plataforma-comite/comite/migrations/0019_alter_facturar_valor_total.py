# Generated by Django 5.1.1 on 2024-10-29 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comite', '0018_alter_facturar_fecha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facturar',
            name='valor_total',
            field=models.IntegerField(default=0, editable=False),
        ),
    ]
