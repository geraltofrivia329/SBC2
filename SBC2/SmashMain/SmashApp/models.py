from django.db import models

class SmashChars(models.Model):
    character_name = models.CharField(max_length = 100)
    description = models.TextField
    image = models.CharField(max_length=100)
