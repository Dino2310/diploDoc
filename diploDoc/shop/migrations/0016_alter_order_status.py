# Generated by Django 5.0.6 on 2024-06-28 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0015_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.TextField(blank=True, choices=[('created', 'Создан'), ('assembling', 'В сборке'), ('delivering', 'В пути'), ('arrived', 'В пункте выдачи'), ('received', 'Получен'), ('cancelled', 'Отменен'), ('returned', 'Возврат')], default='created', max_length=255, null=True, verbose_name='Статус заказа'),
        ),
    ]
