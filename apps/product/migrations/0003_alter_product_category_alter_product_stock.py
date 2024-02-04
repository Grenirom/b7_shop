# Generated by Django 5.0.1 on 2024-01-31 08:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0002_alter_category_name_alter_category_parent'),
        ('product', '0002_alter_product_article_alter_product_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='categories.category', verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='product',
            name='stock',
            field=models.CharField(blank=True, choices=[('in_stock', 'В наличии!'), ('out_of_stock', 'Нет в наличии!')], max_length=20, null=True, verbose_name='Наличие'),
        ),
    ]