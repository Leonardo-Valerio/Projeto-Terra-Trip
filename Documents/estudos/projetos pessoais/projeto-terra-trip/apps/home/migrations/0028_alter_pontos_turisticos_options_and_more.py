# Generated by Django 5.0.1 on 2024-01-30 00:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0027_alter_pontos_turisticos_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pontos_turisticos',
            options={},
        ),
        migrations.AlterField(
            model_name='pontos_turisticos',
            name='cidade_relacionada',
            field=models.ForeignKey(limit_choices_to=models.Q(('cidade_relacionada__isnull', True), ('cidade_relacionada__pais_relacionado', models.F('cidade_relacionada__pais_relacionado')), _connector='OR'), null=True, on_delete=django.db.models.deletion.CASCADE, to='home.cidades'),
        ),
    ]