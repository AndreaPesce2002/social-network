# Generated by Django 4.1.7 on 2023-03-31 12:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0010_alter_post_datapubblicazione'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='dataPubblicazione',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 31, 12, 13, 45, 241696, tzinfo=datetime.timezone.utc)),
        ),
    ]