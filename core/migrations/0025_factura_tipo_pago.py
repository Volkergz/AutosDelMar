# Generated by Django 5.0.6 on 2024-07-13 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0024_remove_factura_tipo_pago_factura_num_tarjeta'),
    ]

    operations = [
        migrations.AddField(
            model_name='factura',
            name='tipo_pago',
            field=models.CharField(default='Efectivo', max_length=50),
        ),
    ]
