# Generated by Django 5.0.1 on 2024-01-22 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='categoria',
            field=models.CharField(choices=[('PAÍS', 'País'), ('CONTINENTE', 'Continente')], default='', max_length=100),
        ),
    ]
