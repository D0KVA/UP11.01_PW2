# Generated by Django 5.2.3 on 2025-06-10 13:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название категории')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Имя коллекции')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Коллекция',
                'verbose_name_plural': 'Коллекции',
            },
        ),
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Имя позиции')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('price', models.FloatField(verbose_name='Цена')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='image/%Y/%m/%d', verbose_name='Изоборажение')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления на сайт')),
                ('is_exists', models.BooleanField(default=True, verbose_name='Доступность к заказу')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='shop.category', verbose_name='Кстегория')),
            ],
            options={
                'verbose_name': 'Предмет',
                'verbose_name_plural': 'Предметы',
            },
        ),
    ]
