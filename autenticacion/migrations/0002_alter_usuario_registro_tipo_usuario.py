# Generated by Django 4.2.16 on 2024-11-15 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autenticacion', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario_registro',
            name='tipo_usuario',
            field=models.CharField(choices=[('Trabajador', 'Trabajador'), ('Jefe', 'Jefe'), ('Administrador Informático', 'Administrador Informático'), ('Administrador Operacional', 'Administrativo Operacional')], default='Trabajador', max_length=30),
        ),
    ]
