# Generated by Django 4.1.7 on 2023-04-03 10:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0016_alter_post_datapubblicazione'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='dataPubblicazione',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 3, 10, 9, 20, 427140, tzinfo=datetime.timezone.utc)),
        ),
    ]
