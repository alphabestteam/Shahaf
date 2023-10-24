from django.db import models
from users import User

status_options = {
    'closed': 'Closed',
    'open': 'Open',
    'waiting for response': 'Waiting for response',
    'waiting for treatment': 'Waiting for treatment'
}
class Form(models.Model):
    open_date = models.DateField()
    close_date = models.DateField()
    report_username = models.CharField(max_length=50)
    status = models.CharField(choices= status_options)
    can_open_event = models.BooleanField(default= False)
    can_download_event = models.BooleanField(default= False)
    users = models.ManyToManyField(User, related_name= 'users')
