# Generated by Django 5.0.1 on 2024-01-29 22:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0018_alter_pontos_turisticos_latitude_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pontos_turisticos',
            name='pais_relacionado',
        ),
        migrations.CreateModel(
            name='Cidades',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('legenda', models.CharField(max_length=250)),
                ('pais_relacionado', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='home.paises')),
            ],
        ),
        migrations.AddField(
            model_name='pontos_turisticos',
            name='cidade_relacionada',
            field=models.ForeignKey(default='', null = True , on_delete=django.db.models.deletion.CASCADE, to='home.cidades'),
        ),
    ]