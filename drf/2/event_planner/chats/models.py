from django.db import models

class Chat(models.Model):
    id = models.CharField(primary_key= True, max_length= 255)
    messages = models.ForeignKey('message.Message', on_delete = models.SET_NULL, null= True, related_name = 'chat_messages')