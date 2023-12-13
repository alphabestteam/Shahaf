from rest_framework import serializers
from .models import Comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

    def update(self, instance, validated_data):
        instance.user_id = validated_data.get('user_id', instance.user_id)
        instance.text = validated_data.get('text', instance.text)
        instance.stars = validated_data.get('stars', instance.stars)
        instance.recipe_id = validated_data.get('recipe_id', instance.recipe_id)
        instance.comment_id = validated_data.get('comment_id', instance.comment_id)
        return instance