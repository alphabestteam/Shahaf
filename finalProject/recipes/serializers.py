from rest_framework import serializers
from .models import Recipe

class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = '__all__'

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.ingredients = validated_data.get('ingredients', instance.ingredients)
        instance.preparation = validated_data.get('preparation', instance.preparation)
        instance.type = validated_data.get('type', instance.type)
        instance.time = validated_data.get('time', instance.time)
        instance.level = validated_data.get('level', instance.level)
        instance.avg_starts = validated_data.get('avg_starts', instance.avg_starts)
        if instance.recipe_comments is not None:
            instance.recipe_comments.set(validated_data.get('recipe_comments', instance.recipe_comments))
        else:
            instance.recipe_comments = validated_data.get(validated_data.get('recipe_comments', instance.recipe_comments))
        instance.recipe_id = validated_data.get('recipe_id', instance.recipe_id)
        instance.save()
        return instance