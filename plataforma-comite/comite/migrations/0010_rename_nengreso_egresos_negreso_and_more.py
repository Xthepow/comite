# Generated by Django 5.1.1 on 2024-09-26 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comite', '0009_vacunadores_vacunas_egresos'),
    ]

    operations = [
        migrations.RenameField(
            model_name='egresos',
            old_name='nEngreso',
            new_name='nEgreso',
        ),
        migrations.RemoveField(
            model_name='egresos',
            name='valorIngreso',
        ),
        migrations.AddField(
            model_name='egresos',
            name='valorEngreso',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]