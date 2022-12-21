from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) #Se l'utente viene cancellato, anche tutti i suoi poste vengono eliminati
    datetime = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
