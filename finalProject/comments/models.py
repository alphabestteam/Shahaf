from django.db import models
from users import User
from recipes import Recipe

class Comment(models.Model):
    user_id = models.OneToOneField(User, related_name= 'user_id', on_delete=models.CASCADE, blank = False)
    text = models.TextField(blank= False)
    stars = models.PositiveIntegerField(blank= False, limit_value = 5)
    recipe_id = models.OneToOneField(Recipe, related_name= 'recipe_id', on_delete=models.CASCADE, blank = False)
    comment_id = models.AutoField(primary_key= True)