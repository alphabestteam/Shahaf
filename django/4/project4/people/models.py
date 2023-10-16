from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    city = models.CharField(max_length = 50)
    id = models.CharField(max_length = 9, primary_key = True)


    def __str__(self) -> str:
        return f'name: {self.name} date of birth: {self.date_of_birth} city: {self.city} id: {self.id}'
