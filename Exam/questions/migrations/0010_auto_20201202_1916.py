# Generated by Django 3.1.3 on 2020-12-02 13:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0009_auto_20201202_1912'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam_model',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 2, 19, 16, 52, 909897)),
        ),
        migrations.AlterField(
            model_name='exam_model',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 2, 19, 16, 52, 909897)),
        ),
    ]
