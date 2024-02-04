# Generated by Django 5.0.1 on 2024-01-30 08:45

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('article', models.CharField(max_length=20, validators=[django.core.validators.RegexValidator('^[0-9!@#$%^&*()-_+=?]+$')])),
                ('price', models.PositiveIntegerField()),
                ('quantity', models.IntegerField(default=0)),
                ('description', models.TextField()),
                ('tech_characteristics', models.TextField(blank=True, null=True)),
                ('dop_info', models.TextField(blank=True, null=True)),
                ('stock', models.CharField(blank=True, choices=[('in_stock', 'В наличии!'), ('out_of_stock', 'Нет в наличии!')], max_length=20, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='categories.category')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
            },
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='media/product-images/')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='product.product')),
            ],
        ),
        migrations.CreateModel(
            name='ProductSize',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(blank=True, max_length=20, null=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_sizes', to='product.product')),
            ],
        ),
    ]