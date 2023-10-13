from django.db import models

class Target(models.Model):
    # Implement here a target model with a __str__ function
    name = models.CharField(max_length=100),
    description = models.TextField(blank = False, null = False),
    prioritization = models.CharField(max_length=1),
    is_destroyed = models.BooleanField(blank = False, null = False),
    x_coordinate = models.CharField(max_length=100),
    y_coordinate = models.CharField(max_length=100),

    def __str__(self) -> str:
        return super().__str__()