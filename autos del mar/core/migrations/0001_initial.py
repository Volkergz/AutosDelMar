# Generated by Django 5.0.6 on 2024-06-27 04:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('producto_id', models.IntegerField(primary_key=True, serialize=False)),
                ('Precio', models.IntegerField()),
                ('descripcion', models.CharField(max_length=250)),
                ('cantidad', models.IntegerField()),
                ('estado_producto', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Tipo_usuario',
            fields=[
                ('id_tipo_usuario', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre_tipo_usuario', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('usuario_id', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('apellidop', models.CharField(max_length=50)),
                ('apellidom', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=150)),
                ('nr_telefono', models.CharField(max_length=15)),
                ('contraseña', models.CharField(max_length=50)),
                ('estado_usuario', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Accesorios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('distribuidor', models.CharField(max_length=100)),
                ('producto_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.producto')),
            ],
        ),
        migrations.CreateModel(
            name='Vehiculo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=100)),
                ('modelo', models.CharField(max_length=100)),
                ('producto_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.producto')),
            ],
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('venta_id', models.IntegerField(primary_key=True, serialize=False)),
                ('fecha_venta', models.DateField()),
                ('total_venta', models.IntegerField()),
                ('cliente_run', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Venta_Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad_producto', models.IntegerField()),
                ('subtotal_producto', models.IntegerField()),
                ('producto_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.venta')),
                ('venta_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.producto')),
            ],
        ),
    ]