# Generated by Django 5.0.1 on 2024-01-30 00:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0028_alter_pontos_turisticos_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pontos_turisticos',
            name='pais_relacionado',
        ),
        migrations.AlterField(
            model_name='pontos_turisticos',
            name='cidade_relacionada',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.cidades'),
        ),
    ]
