from django.db import models
from chats import Chat
from users import User

class Message(models.Model):
    text = models.TextField()
    sending_date = models.DateField()
    chat_pointer = models.ForeignKey(Chat)
    sender = models.OneToOneField(User)
