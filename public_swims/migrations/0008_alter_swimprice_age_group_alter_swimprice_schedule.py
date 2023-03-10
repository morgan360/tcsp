# Generated by Django 4.1.5 on 2023-03-10 10:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('public_swims', '0007_alter_swimprice_age_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='swimprice',
            name='age_group',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='public_swims.agegroup'),
        ),
        migrations.AlterField(
            model_name='swimprice',
            name='schedule',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prices', to='public_swims.swimschedule'),
        ),
    ]