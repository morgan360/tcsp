# Generated by Django 4.1.5 on 2023-03-09 19:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age_group', models.CharField(choices=[('SR', 'Senior'), ('AD', 'Adult'), ('CH', 'Child'), ('U3', 'Under 3')], max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='PublicSwim',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('slug', models.SlugField(blank=True, max_length=200)),
                ('image', models.ImageField(blank=True, upload_to='products/%Y/%m/%d')),
                ('description', models.TextField(blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Public Swimming',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='SwimSchedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.TimeField(blank=True)),
                ('end_time', models.TimeField(blank=True)),
                ('day_of_week', models.CharField(blank=True, choices=[('mon', 'Monday'), ('tue', 'Tuesday'), ('wed', 'Wednesday'), ('thu', 'Thursday'), ('fri', 'Friday'), ('sat', 'Saturday'), ('sun', 'Sunday')], max_length=3)),
                ('num_places', models.IntegerField(null=True)),
                ('active', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('swim', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='public_swims.publicswim')),
            ],
        ),
        migrations.CreateModel(
            name='SwimCustomer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('age_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='public_swims.customertype')),
                ('swim', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='public_swims.publicswim')),
            ],
        ),
        migrations.AddIndex(
            model_name='publicswim',
            index=models.Index(fields=['id', 'slug'], name='public_swim_id_eb21c1_idx'),
        ),
        migrations.AddIndex(
            model_name='publicswim',
            index=models.Index(fields=['name'], name='public_swim_name_7bdad5_idx'),
        ),
        migrations.AddIndex(
            model_name='publicswim',
            index=models.Index(fields=['-created'], name='public_swim_created_542b44_idx'),
        ),
    ]