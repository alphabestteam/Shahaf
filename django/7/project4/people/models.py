from django.db import models
from django.core.validators import MaxValueValidator

class Person(models.Model):
    name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    city = models.CharField(max_length = 50)
    id = models.CharField(max_length = 9, primary_key = True)


    def __str__(self) -> str:
        return f'name: {self.name} date of birth: {self.date_of_birth} city: {self.city} id: {self.id}'


class Parent(Person):
    place_of_work = models.CharField(max_length=50)
    salary = models.IntegerField(MaxValueValidator(999999))
    children = models.ManyToManyField(Person, related_name='parents', blank = True)

    def __str__(self):
        return f'parent info: name: {self.name} date of birth: {self.date_of_birth} city: {self.city} id: {self.id} place of work: {self.place_of_work} salary: {self.salary} with children: {self.children.all().values()}'