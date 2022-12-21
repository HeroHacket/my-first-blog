from django.conf import settings
from django.db import models
from django.utils import timezone

"""
models.CharField - così si definisce un testo con un numero limitato di lettere.
models.TextField - questo è il codice per definire un testo senza un limite. Sembra l'ideale per i contenuti di un post, vero?
models.DateTimeField - questo per la data ed l'ora.
models.ForeignKey - questo è un link a un altro modello.
"""

class PostT(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
