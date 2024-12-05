# Generated by Django 3.2.9 on 2024-11-10 02:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel_app', '0002_auto_20241110_0239'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='image',
            field=models.ImageField(blank=True, default='/images/placeholder.png', null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='checkin_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 11, 10, 5, 0, 17, 340747)),
        ),
        migrations.AlterField(
            model_name='booking',
            name='checkout_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 11, 11, 5, 0, 17, 340747)),
        ),
    ]
