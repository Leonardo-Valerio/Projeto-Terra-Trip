# Generated by Django 5.0.1 on 2024-03-04 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roteiros', '0007_alter_roteiro_grupo_paises'),
    ]

    operations = [
        migrations.AddField(
            model_name='roteiro',
            name='roteiro_gerado',
            field=models.TextField(blank=True, null=True),
        ),
    ]
