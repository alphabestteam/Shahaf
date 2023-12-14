from django.db import models
from django import forms 

RECIPE_TYPE = (
    ('1', 'Cake'),
    ('2', 'Pie'),
    ('3', 'Cookie'),
    ('4', 'Cupcakes'),
    ('5', 'Pastries'),
    ('6', 'Other')
)

LEVELS = (
    ('1', 'Beginner'),
    ('2', 'Intermediate'),
    ('3', 'Advanced'),
)

def validate_max(value):
    return value <= 5

class Recipe(models.Model):
    name = models.CharField(max_length= 50, blank = False)
    ingredients = models.TextField(blank = False)
    preparation = models.TextField(blank = False)
    type = forms.MultipleChoiceField(choices = RECIPE_TYPE)
    time = models.TimeField(blank = False)
    level = forms.MultipleChoiceField(choices = LEVELS)
    avg_starts = models.IntegerField(blank = True, validators=[validate_max], editable=False)
    sum_stars = models.IntegerField(blank = True, default= 0, editable=False)
    comments_number = models.IntegerField(blank = True, default= 0, editable=False)
    recipe_comments = models.ForeignKey('comments.Comment', related_name='recipe_comments', on_delete=models.CASCADE, blank = True, editable=False)
    recipe_id = models.AutoField(primary_key= True, blank= False)