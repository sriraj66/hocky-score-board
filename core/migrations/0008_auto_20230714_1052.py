# Generated by Django 3.2.16 on 2023-07-14 05:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_delete_timer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Timer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('min', models.PositiveIntegerField(default=0)),
                ('sec', models.PositiveIntegerField(default=0)),
                ('total_sec', models.PositiveIntegerField(default=0)),
                ('is_running', models.BooleanField(default=False)),
                ('is_pause', models.BooleanField(default=False)),
                ('remaining_time', models.PositiveIntegerField(default=0)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.AddField(
            model_name='match',
            name='timer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.timer'),
        ),
    ]
