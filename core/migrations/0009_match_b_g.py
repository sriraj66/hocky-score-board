# Generated by Django 3.2.16 on 2023-07-14 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20230714_1052'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='b_g',
            field=models.CharField(default='#33cc33', max_length=20, verbose_name='Background Color'),
        ),
    ]
