from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.password = validated_data.get('password', instance.password)
        instance.birthday = validated_data.get('birthday', instance.birthday)
        instance.email = validated_data.get('email', instance.email)
        instance.my_recipes.set(validated_data.get('my_recipes', instance.my_recipes))
        instance.id = validated_data.get('id', instance.id)
        instance.save()
        return instance