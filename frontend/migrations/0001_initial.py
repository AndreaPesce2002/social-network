import datetime
from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Utente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('descrizione', models.CharField(max_length=200)),
                ('followers', models.ManyToManyField(blank=True, default=[], related_name='following', to='frontend.Utente')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.ImageField(upload_to='')),
                ('descrizione', models.CharField(max_length=200)),
                ('dataPubblicazione', models.DateTimeField(default=datetime.datetime(2023, 10, 5, 14, 2, 38, 782330, tzinfo=datetime.timezone.utc))),
                ('creatore', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='frontend.Utente')),
                ('like', models.ManyToManyField(blank=True, related_name='liked_by', to='frontend.Utente')),
            ],
            options={
                'ordering': ['-dataPubblicazione'],
            },
        ),
    ]