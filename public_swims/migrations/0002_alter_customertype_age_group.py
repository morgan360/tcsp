# Generated by Django 4.1.5 on 2023-03-09 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('public_swims', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customertype',
            name='age_group',
            field=models.CharField(max_length=10),
        ),
    ]
