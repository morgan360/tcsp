# Generated by Django 4.1.5 on 2023-03-10 10:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('public_swims', '0006_remove_swimschedule_price_swimprice_schedule'),
    ]

    operations = [
        migrations.AlterField(
            model_name='swimprice',
            name='age_group',
            field=models.ForeignKey(default='adult', on_delete=django.db.models.deletion.CASCADE, to='public_swims.agegroup'),
        ),
    ]