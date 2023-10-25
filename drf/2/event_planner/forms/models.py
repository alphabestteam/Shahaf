from django.db import models

status_options = [
    ('closed', 'Closed'),
    ('open', 'Open'),
    ('waiting for response', 'Waiting for response'),
    ('waiting for treatment', 'Waiting for treatment')
]

class Form(models.Model):
    open_date = models.DateField()
    close_date = models.DateField()
    report_username = models.CharField(max_length=50)
    status = models.CharField(choices= status_options, max_length= 255)
    can_open_event = models.BooleanField(default= False)
    can_download_event = models.BooleanField(default= False)
    users = models.ManyToManyField('users.User', related_name= 'form_users')
    id = models.CharField(primary_key= True, max_length= 255)

class ChatForm(Form):
    chats = models.ManyToManyField('chats.Chat', related_name= 'form_chats')

class FileForm(Form):
    files = models.ManyToManyField('message.File', related_name= 'form_files')