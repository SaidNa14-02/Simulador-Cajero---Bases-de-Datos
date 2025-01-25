# Generated by Django 4.2 on 2025-01-25 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cajero_Pichincha', '0002_alter_user_options_alter_user_identification'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'Usuario', 'verbose_name_plural': 'Usuarios'},
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='Correo electrónico'),
        ),
        migrations.AlterField(
            model_name='user',
            name='identification',
            field=models.CharField(blank=True, max_length=10, null=True, unique=True, verbose_name='Identificación'),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Número de teléfono'),
        ),
    ]
