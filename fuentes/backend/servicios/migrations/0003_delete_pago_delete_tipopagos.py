# Generated by Django 5.1 on 2024-08-09 05:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('servicios', '0002_alter_pago_fecha_pago'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Pago',
        ),
        migrations.DeleteModel(
            name='TipoPagos',
        ),
    ]
