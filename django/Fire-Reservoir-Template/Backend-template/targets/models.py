from django.db import models

class Target(models.Model):
    name = models.CharField(max_length=100)
    attack_priority = models.CharField(max_length=2)
    longitude = models.CharField(max_length = 100)
    latitude = models.CharField(max_length = 100)
    enemy_organization = models.CharField(max_length=100)
    target_goal = models.CharField(max_length=100)
    was_target_destroyed = models.BooleanField(blank = False)
    target_id = models.IntegerField(primary_key = True)


    def __str__(self) -> str:
        return f'name: {self.name}, attack priority: {self.attack_priority}, latitude: {self.latitude}, longitude: {self.longitude}, enemy organization: {self.enemy_organization}, target goal: {self.target_goal}, target id: {self.target_id}, is destroyed: {self.is_destroyed}'
