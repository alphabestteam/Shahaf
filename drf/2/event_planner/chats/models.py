from django.db import models

class Message(models.Model):
    id = models.CharField(primary_key= True)
