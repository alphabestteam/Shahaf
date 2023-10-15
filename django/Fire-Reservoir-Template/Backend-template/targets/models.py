from django.db import models

class Target(models.Model):
    name = models.CharField(max_length=100, null= True)
    attack_priority = models.CharField(max_length=2, null= True)
    longitude = models.CharField(max_length = 100, null = True)
    latitude = models.CharField(max_length = 100, null = True)
    enemy_organization = models.CharField(max_length=100, null= True)
    target_goal = models.CharField(max_length=100, null= True)
    was_target_destroyed = models.BooleanField(blank = False, null= True)
    target_id = models.IntegerField(null = False, primary_key = True)


    def __str__(self) -> str:
        return f'name: {self.name}, attack priority: {self.attack_priority}, latitude: {self.latitude}, longitude: {self.longitude}, enemy organization: {self.enemy_organization}, target goal: {self.target_goal}, target id: {self.target_id}, is destroyed: {self.is_destroyed}'
