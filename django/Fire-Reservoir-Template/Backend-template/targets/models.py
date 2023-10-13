from django.db import models

class Target(models.Model):
    # Implement here a target model with a __str__ function
    name = models.CharField(max_length=100),
    attack_priority = models.CharField(max_length=2, min_length = 1),
    latitude = models.CharField(max_length = 100, null = False),
    longitude = models.CharField(max_length = 100, null = False),
    enemy_organization = models.CharField(max_length=100),
    target_goal = models.CharField(max_length=100),
    target_id = models.CharField(null = False, min_length = 1)
    is_destroyed = models.BooleanField(blank = False, null = False),

    def __str__(self) -> str:
        return super().__str__()