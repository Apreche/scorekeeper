from django.db import models
from django.contrib.auth.models import User

class Player(models.Model):
    name = models.CharField(max_length=255, unique=True)
    user = models.ForeignKey(User, unique=True)

    def __unicode__(self):
        return self.name
