from rest_framework import serializers
from .models import Target

class TargetSerializer(serializers.ModelSerializer):
    class Meta:
        Model = Target
        Fields = ('name', 'description', 'prioritization', 'is_destroyed', 'x_coordinate', 'y_coordinate')

    def create(self, validated_data):
        return Target(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.prioritization = validated_data.get('prioritization', instance.prioritization)
        instance.is_destroyed = validated_data.get('is_destroyed', instance.is_destroyed)
        instance.x_coordinate = validated_data.get('x_coordinate', instance.x_coordinate)
        instance.y_coordinate = validated_data.get('y_coordinate', instance.y_coordinate)
        return instance
    