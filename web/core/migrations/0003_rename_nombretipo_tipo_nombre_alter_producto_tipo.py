# Generated by Django 4.0.5 on 2022-06-28 08:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_contactos_aviso_alter_contactos_fecha_enviado_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tipo',
            old_name='nombreTipo',
            new_name='nombre',
        ),
        migrations.AlterField(
            model_name='producto',
            name='tipo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.tipo'),
        ),
    ]