from django.db import models

class User(models.Model):
    username = models.CharField(max_length = 15, blank = False)
    password = models.TextField(blank = False)
    birthday = models.DateField(blank = False)
    email = models.EmailField(blank = False)
    my_recipes = models.ManyToManyField('recipes.Recipe', related_name='favorite_recipes', blank=True)
    id = models.PositiveIntegerField(max_length = 9, blank = False, unique = True, primary_key = True)