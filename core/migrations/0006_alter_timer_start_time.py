# Generated by Django 3.2.16 on 2023-07-13 16:33

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_remove_timer_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timer',
            name='start_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
