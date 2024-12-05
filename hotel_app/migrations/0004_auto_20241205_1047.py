# Generated by Django 3.2.9 on 2024-12-05 07:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel_app', '0003_auto_20241110_0500'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='room',
            options={'verbose_name': 'hotel Room'},
        ),
        migrations.AlterField(
            model_name='booking',
            name='checkin_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 12, 5, 10, 47, 22, 773402)),
        ),
        migrations.AlterField(
            model_name='booking',
            name='checkout_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 12, 6, 10, 47, 22, 773402)),
        ),
    ]
