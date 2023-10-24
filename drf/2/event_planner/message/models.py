from django.db import models

class Message(models.Model):
    text = models.TextField()
    sending_date = models.DateField()
    chat_pointer = models.ForeignKey('chats.Chat', on_delete = models.SET_NULL, null= True)
    sender = models.ForeignKey('users.User', on_delete = models.SET_NULL, null= True, related_name='messages_sender')
    receiver = models.ForeignKey('users.User', on_delete = models.SET_NULL, null= True, related_name='messages_receiver')
    is_read = models.BooleanField(default= False)
    id = models.CharField(primary_key= True, max_length= 255)

class File(models.Model):
    upload_date = models.DateField()
    sender = models.ForeignKey('users.User', on_delete = models.SET_NULL, null= True)
    file = models.FileField()
    id = models.CharField(primary_key= True, max_length= 255)
