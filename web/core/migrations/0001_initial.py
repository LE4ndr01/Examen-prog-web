# Generated by Django 4.0.5 on 2022-06-16 08:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contactos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('tipo_consulta', models.IntegerField(choices=[[0, 'Consulta'], [1, 'Sugerencia'], [2, 'Reclamo'], [3, 'otro'], [4, 'No deseo responder']])),
                ('mensajes', models.TextField(max_length=500)),
                ('aviso', models.BooleanField()),
                ('fecha_enviado', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='tipo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreTipo', models.CharField(max_length=50, verbose_name='Nombre Tipo')),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('precio', models.IntegerField()),
                ('descripcion', models.TextField()),
                ('seg_desc', models.TextField()),
                ('nuevo', models.BooleanField()),
                ('fecha_ingresado', models.DateField()),
                ('imagen', models.ImageField(null=True, upload_to='producto')),
                ('fecha', models.DateField(auto_now_add=True)),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.tipo')),
            ],
        ),
    ]