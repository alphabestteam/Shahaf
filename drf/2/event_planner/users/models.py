from django.db import models
from message import Message

class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    id = models.CharField(max_length = 9, primary_key = True)
    email = models.EmailField(max_length=254)
    unread_messages = models.ManyToManyField(Message, related_name= 'messages')