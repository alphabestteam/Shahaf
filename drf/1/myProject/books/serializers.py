from rest_framework import serializers
from .models import Book
from datetime import date

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    def create(self, validated_data):
        return Book(**validated_data)
    
    #Q10:
    def validate_publication_date(self, publication_year):
        current_year = date.today().year

        if publication_year > current_year:
            raise serializers.ValidationError("publication year is not valid!")
        
        return publication_year
    
    #Q11:
    #to update only one field we can use partial update with partial=True. example:
    #serializer_update = BookSerializer(book, data = {'publication_date': '2001-01-01'}, partial=True)

    #Q12:
    #to generate nested representations we can use depth. it should be set to an integer that indicates the depth of relationships that should be traversed before reverting to a flat representation.

    #