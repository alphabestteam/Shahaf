from django.db import models
from django import forms 

STARS = (
    ('1', 1),
    ('2', 2),
    ('3', 3),
    ('4', 4),
    ('5', 5),
)

class Comment(models.Model):
    user_id = models.ForeignKey('users.User', related_name= 'comment_user_id', on_delete=models.CASCADE, blank = False)
    text = models.TextField(blank= False)
    stars = forms.MultipleChoiceField(choices = STARS)
    recipe_id = models.ForeignKey('recipes.Recipe', related_name= 'comment_recipe_id', on_delete=models.CASCADE, blank = False)
    comment_id = models.AutoField(primary_key= True, blank= False)