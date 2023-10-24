from django.db import models

class Chat(models.Model):
    id = models.CharField(primary_key= True, max_length= 255)