# Generated by Django 5.0.1 on 2024-01-31 20:37

import django.db.models.deletion
import django.db.models.expressions
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0033_alter_cidades_legenda'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pontos_turisticos',
            name='cidade_relacionada',
            field=models.ForeignKey(blank=True, limit_choices_to={'pais_relacionado': django.db.models.expressions.OuterRef('cidade_relacionada__pais_relacionado')}, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.cidades'),
        ),
    ]