# Generated by Django 5.0.1 on 2024-01-24 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_delete_topico_remove_paises_topicos_paises_inverno_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='paises',
            name='choque_cultural',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='paises',
            name='outono',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='paises',
            name='primavera',
            field=models.BooleanField(default=False),
        ),
    ]
