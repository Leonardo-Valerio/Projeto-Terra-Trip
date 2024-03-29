# Generated by Django 5.0.1 on 2024-01-23 18:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_card_legenda_alter_card_descricao'),
    ]

    operations = [
        migrations.CreateModel(
            name='Continentes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('imagem', models.ImageField(blank=True, upload_to='fotos/%Y/%m/%d/')),
                ('legenda', models.CharField(max_length=250)),
                ('descricao', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Paises',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('imagem', models.ImageField(blank=True, upload_to='fotos-paises/%Y/%m/%d')),
                ('legenda', models.CharField(max_length=250)),
                ('descricao', models.TextField()),
                ('continente_relacionado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.continentes')),
            ],
        ),
        migrations.CreateModel(
            name='Pontos_turisticos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('imagem', models.ImageField(blank=True, upload_to='fotos_pontos-turisticos/%Y/%m/%d')),
                ('legenda', models.CharField(max_length=250)),
                ('descricao', models.TextField()),
                ('pais_relacionado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.paises')),
            ],
        ),
        migrations.DeleteModel(
            name='Card',
        ),
    ]
