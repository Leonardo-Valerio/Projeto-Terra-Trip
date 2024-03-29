# Generated by Django 5.0.1 on 2024-02-26 17:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0036_paises_presente_na_home'),
        ('roteiros', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roteiro',
            name='dias',
            field=models.IntegerField(),
        ),
        migrations.CreateModel(
            name='Viagem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_pais', models.CharField(max_length=100)),
                ('identificador_pais', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.paises')),
            ],
        ),
    ]
