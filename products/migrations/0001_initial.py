# Generated by Django 5.0.1 on 2024-03-28 16:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название товара')),
                ('image', models.ImageField(blank=True, upload_to='products_images/', verbose_name='Изображение')),
                ('description', models.TextField(blank=True, verbose_name='Описание товара')),
                ('prod_description', models.CharField(blank=True, max_length=100, verbose_name='Краткое описание')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name='Цена')),
                ('quantity', models.PositiveIntegerField(default=0, verbose_name='Количество')),
            ],
            options={
                'verbose_name': 'товар',
                'verbose_name_plural': 'Товары',
            },
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Категории')),
                ('description', models.TextField(blank=True, verbose_name='Описание категории')),
            ],
            options={
                'verbose_name': 'категории',
                'verbose_name_plural': 'Категорию',
            },
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_photo', models.ImageField(blank=True, upload_to='products_images/add/', verbose_name='Фото')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product', verbose_name='Товар')),
            ],
            options={
                'verbose_name': 'изображение',
                'verbose_name_plural': 'Изображения',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.productcategory', verbose_name='Категория'),
        ),
    ]
