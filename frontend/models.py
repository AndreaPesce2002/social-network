from django.contrib.auth.hashers import make_password
from django.utils import timezone
from django.db import models
import datetime
datetime.datetime.now()

# Create your models here.
class Utente(models.Model):
    nome = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    descrizione=models.CharField(max_length=200)
    followers = models.ManyToManyField('self', related_name='following', blank=True, default=[], symmetrical=False)

    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def num_follower(self):
        return Utente.objects.filter(followers=self).count()

class Post(models.Model):
    creatore  = models.ForeignKey(Utente, on_delete=models.CASCADE)
    post = models.ImageField()
    descrizione = models.CharField(max_length=200)
    like = models.IntegerField(default=0)
    dataPubblicazione = models.DateTimeField(default=timezone.now())

    class Meta:
        ordering = ['-dataPubblicazione']

    def add_like(self):
        self.likes += 1
        self.save()
    
    def time_passed(self):
        now = timezone.now()
        delta = now - self.dataPubblicazione
        seconds = delta.total_seconds()

        if seconds < 60:
            return f"{int(seconds)}s fa"
        elif seconds < 3600:
            return f"{int(seconds / 60)}m fa"
        elif seconds < 86400:
            return f"{int(seconds / 3600)}h fa"
        else:
            return f"{int(seconds / 86400)}gg fa"