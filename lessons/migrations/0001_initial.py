# Generated by Django 4.1.5 on 2023-03-08 12:10

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=200, unique=True)),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, null=True)),
                ('short_name', models.CharField(max_length=3, null=True)),
                ('day_no', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(6), django.core.validators.MinValueValidator(0)])),
            ],
            options={
                'verbose_name_plural': 'Days',
            },
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, null=True)),
            ],
            options={
                'verbose_name_plural': 'Lessons',
            },
        ),
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, null=True)),
            ],
            options={
                'verbose_name_plural': 'Modules',
            },
        ),
        migrations.CreateModel(
            name='Term',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('rebook_start_date', models.DateField()),
                ('rebook_switch_date', models.DateField()),
            ],
            options={
                'verbose_name_plural': 'Terms',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('num_places', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(16), django.core.validators.MinValueValidator(1)])),
                ('num_weeks', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(16), django.core.validators.MinValueValidator(1)])),
                ('slug', models.SlugField(blank=True, max_length=200)),
                ('image', models.ImageField(blank=True, upload_to='products/%Y/%m/%d')),
                ('start_time', models.TimeField(blank=True, default=None, help_text='Enter a time (hours:minutes)', null=True, verbose_name='Time')),
                ('end_time', models.TimeField()),
                ('description', models.TextField(blank=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('available', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='lessons.category')),
                ('day', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='lessons.day')),
                ('lesson', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='lessons.lesson')),
            ],
            options={
                'verbose_name_plural': 'Products',
                'ordering': ['name'],
            },
        ),
        migrations.AddField(
            model_name='lesson',
            name='module',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lessons.module'),
        ),
        migrations.AddIndex(
            model_name='category',
            index=models.Index(fields=['name'], name='lessons_cat_name_f91e23_idx'),
        ),
        migrations.AddIndex(
            model_name='product',
            index=models.Index(fields=['id', 'slug'], name='lessons_pro_id_9a2e47_idx'),
        ),
        migrations.AddIndex(
            model_name='product',
            index=models.Index(fields=['name'], name='lessons_pro_name_fb7aec_idx'),
        ),
        migrations.AddIndex(
            model_name='product',
            index=models.Index(fields=['-created'], name='lessons_pro_created_6b811b_idx'),
        ),
    ]
