# Generated by Django 5.0.6 on 2024-06-29 02:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_alter_vehiculo_anio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='producto_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
