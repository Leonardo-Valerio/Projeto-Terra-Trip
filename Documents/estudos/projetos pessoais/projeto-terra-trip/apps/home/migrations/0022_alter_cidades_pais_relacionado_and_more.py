# Generated by Django 5.0.1 on 2024-01-29 23:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0021_alter_cidades_pais_relacionado_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cidades',
            name='pais_relacionado',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.paises'),
        ),
        migrations.AlterField(
            model_name='pontos_turisticos',
            name='cidade_relacionada',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.cidades'),
        ),
    ]
