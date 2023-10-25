from django.db import models
from message.models import Message

class Chat(models.Model):
    id = models.CharField(primary_key= True, max_length= 255)
    messages = models.ManyToManyField('message.Message', null= True, related_name = 'chat_messages', blank= True)