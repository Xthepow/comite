# Generated by Django 5.1.1 on 2024-10-31 00:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comite', '0027_rename_info_biologicos_facturar_biologicosinformacion'),
    ]

    operations = [
        migrations.RenameField(
            model_name='biologicos',
            old_name='valor_unitario',
            new_name='valorUnidad',
        ),
        migrations.AlterField(
            model_name='biologicos',
            name='descripcion',
            field=models.TextField(max_length=200),
        ),
    ]