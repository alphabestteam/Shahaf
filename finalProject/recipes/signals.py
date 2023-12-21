from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from .models import Recipe
from django.shortcuts import get_object_or_404
from comments.models import Comment
 
 
@receiver(post_save, sender=Comment) 
def create_profile(sender, instance, created, **kwargs):
    if created:
        recipe = instance.recipe_id
        if recipe.recipe_comments is not None:
            recipe.recipe_comments.add(instance)
        else:
            recipe.recipe_comments.set(instance)
        recipe.comments_number += 1
        recipe.sum_stars += instance.stars
        recipe.save()