# Generated by Django 5.0.1 on 2024-01-28 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_paises_historicos'),
    ]

    operations = [
        migrations.AddField(
            model_name='pontos_turisticos',
            name='iframe_google_maps',
            field=models.TextField(default=''),
        ),
    ]