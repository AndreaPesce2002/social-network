# Generated by Django 4.1.3 on 2023-03-24 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='utente',
            name='followers',
            field=models.ManyToManyField(blank=True, default=[], related_name='following', to='frontend.utente'),
        ),
    ]
