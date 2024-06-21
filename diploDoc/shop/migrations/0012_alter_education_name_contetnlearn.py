# Generated by Django 5.0.6 on 2024-06-21 09:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0011_merge_20240620_1943'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='name',
            field=models.CharField(max_length=200, unique=True, verbose_name='Наменование'),
        ),
        migrations.CreateModel(
            name='ContetnLearn',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, default=None, null=True, upload_to='products/%Y/%m/%d')),
                ('text', models.TextField(blank=True, default=None, null=True)),
                ('queue', models.PositiveSmallIntegerField()),
                ('education', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.education')),
            ],
        ),
    ]
