from rest_framework import serializers
from .models import Person, Parent

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'

    def create(self, validated_data):
        return Person(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.date_of_birth = validated_data.get('date_of_birth', instance.date_of_birth)
        instance.city = validated_data.get('city', instance.city)
        instance.id = validated_data.get('id', instance.id)
        instance.save()
        return instance
    
    class ParentSerializer(serializers.ModelSerializer):
        class Meta:
            model = Parent
            fields = '__all__'

        def create(self, validated_data):
            return Parent(**validated_data)
        
        def update(self, instance, validated_data): #fix
            instance.name = validated_data.get('name', instance.name)
            instance.date_of_birth = validated_data.get('date_of_birth', instance.date_of_birth)
            instance.city = validated_data.get('city', instance.city)
            instance.id = validated_data.get('id', instance.id)
            instance.place_of_work = validated_data.get('place_of_work', instance.place_of_work)
            instance.salary = validated_data.get('salary', instance.salary)
            instance.children = validated_data.get('children', instance.children)
            instance.save()
            return instance