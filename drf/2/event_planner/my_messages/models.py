from django.db import models
from chats import Chat
from users import User

class Message(models.Model):
    text = models.TextField()
    sending_date = models.DateField()
    chat_pointer = models.ForeignKey(Chat)
    sender = models.ForeignKey(User)

class File(models.Model):
    upload_date = models.DateField()
    sender = models.ForeignKey(User)
    file = models.FileField()
