# Generated by Django 3.0.5 on 2020-05-04 14:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_manager', '0010_auto_20200504_1657'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='deadline',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 4, 17, 10, 40, 12043)),
        ),
    ]
