from django.db import models
from django import forms 

RECIPE_TYPE = (
    ('cake', 'Cake'),
    ('pie', 'Pie'),
    ('cookie', 'Cookie'),
    ('cupcakes', 'Cupcakes'),
    ('pastries', 'Pastries'),
    ('other', 'Other')
)

LEVELS = (
    ('beginner', 'Beginner'),
    ('intermediate', 'Intermediate'),
    ('advanced', 'Advanced'),
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
    avg_starts = models.IntegerField(blank = True, validators=[validate_max], editable=False, null=True)
    sum_stars = models.IntegerField(blank = True, default= 0, editable=False, null=True)
    comments_number = models.IntegerField(blank = True, default= 0, editable=False, null=True)
    recipe_comments = models.ManyToManyField('comments.Comment', related_name='recipe_comments', blank = True, editable=False, null=True, default=None)
    recipe_id = models.AutoField(primary_key= True, blank= False)