# Generated by Django 5.0.4 on 2024-05-01 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vpm', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendor',
            name='average_response_time',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='fullfillment_rate',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='on_time_delivery_rate',
            field=models.FloatField(default=0.0),
        ),
    ]
