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

class ChatForm(Form):
    messages = models.ManyToManyField('message.Message', related_name= 'form_messages')

class FileForm(Form):
    files = models.ManyToManyField('message.File', related_name= 'form_files')