# Generated by Django 5.0.6 on 2024-06-11 13:41

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'city',
            },
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('description', models.TextField()),
                ('homework', models.TextField()),
            ],
            options={
                'db_table': 'lesson',
            },
        ),
        migrations.CreateModel(
            name='PayType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'pay_type',
            },
        ),
        migrations.CreateModel(
            name='ProductsProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_code', models.CharField(max_length=20)),
                ('category_name', models.CharField(max_length=50)),
                ('subcategory_code', models.CharField(max_length=20)),
                ('subcategory_name', models.CharField(max_length=50)),
                ('productname', models.CharField(max_length=50)),
                ('photo', models.CharField(blank=True, max_length=255, null=True)),
                ('price', models.IntegerField()),
                ('description', models.CharField(blank=True, max_length=3000, null=True)),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
                'db_table': 'products_product',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='ProductsUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255)),
                ('username', models.CharField(blank=True, max_length=255, null=True)),
                ('telegram_id', models.BigIntegerField(unique=True)),
            ],
            options={
                'verbose_name': 'Product User',
                'verbose_name_plural': 'Product Users',
                'db_table': 'products_user',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='addresses', to='app.city')),
            ],
            options={
                'db_table': 'address',
            },
        ),
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='modules', to='app.lesson')),
            ],
            options={
                'db_table': 'modules',
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('price', models.IntegerField()),
                ('module', models.ManyToManyField(related_name='courses', to='app.module')),
            ],
            options={
                'db_table': 'courses',
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payments', to='app.course')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payments', to=settings.AUTH_USER_MODEL)),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payments', to='app.paytype')),
            ],
            options={
                'db_table': 'payments',
            },
        ),
    ]