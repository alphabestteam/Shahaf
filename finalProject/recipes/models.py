from django.db import models
from comments import Comment

class Recipe(models.Model):
    name = models.CharField(max_length= 50, blank = False)
    ingredients = models.TextField(blank = False)
    preparation = models.TextField(blank = False)
    time = models.TimeField(blank = False)
    level = models.CharField(blank = False)
    avg_starts = models.IntegerField(blank = False, limit_value = 5)
    image = models.ImageField(blank = False)
    recipe_comments = models.ForeignKey(Comment, related_name='recipe_comments', on_delete=models.CASCADE, blank = True)
    recipe_id = models.AutoField(primary_key= True, blank= False)