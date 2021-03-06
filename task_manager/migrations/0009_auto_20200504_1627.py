# Generated by Django 3.0.5 on 2020-05-04 13:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_manager', '0008_auto_20200504_1541'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='deadline',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 4, 16, 27, 36, 251796)),
        ),
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('OPEN', 'Open'), ('IN_P', 'In progress'), ('FIN', 'Finished')], default='OPEN', max_length=4),
        ),
    ]
