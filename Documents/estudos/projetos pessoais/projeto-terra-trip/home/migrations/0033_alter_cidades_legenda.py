# Generated by Django 5.0.1 on 2024-01-31 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0032_remove_pontos_turisticos_descricao_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cidades',
            name='legenda',
            field=models.TextField(),
        ),
    ]
