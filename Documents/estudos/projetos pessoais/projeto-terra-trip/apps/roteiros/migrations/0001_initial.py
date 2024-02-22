# Generated by Django 5.0.1 on 2024-02-21 23:15

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Roteiro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('dias', models.IntegerField(max_length=3)),
                ('epoca', models.CharField(choices=[('verão', 'Verão'), ('inverno', 'Inverno'), ('primavera', 'Primavera'), ('outono', 'Outono')], max_length=10)),
                ('usuario_roteiro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]