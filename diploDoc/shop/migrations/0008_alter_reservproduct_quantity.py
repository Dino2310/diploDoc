# Generated by Django 5.0.6 on 2024-06-17 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_remove_order_quantity_alter_order_delivery_address_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservproduct',
            name='quantity',
            field=models.PositiveSmallIntegerField(default=1, verbose_name='Количество'),
        ),
    ]
