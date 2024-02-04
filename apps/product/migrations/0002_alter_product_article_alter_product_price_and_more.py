# Generated by Django 5.0.1 on 2024-01-31 08:36

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='article',
            field=models.CharField(max_length=20, validators=[django.core.validators.RegexValidator('^[0-9!@#$%^&*()-_+=?]+$')], verbose_name='Артикул'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.PositiveIntegerField(verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='product',
            name='quantity',
            field=models.IntegerField(default=0, verbose_name='Количество товара'),
        ),
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Имя товара'),
        ),
    ]
