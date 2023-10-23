from rest_framework import serializers
from .models import Book
from django.utils import timezone

#Q16:
# class AuthorSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Author
#         fields = ['name']

class BookSerializer(serializers.ModelSerializer):
    #Q13:
    # publication = serializers.CharField(max_length=255)
    #Q15:
    # book_and_author = serializers.SerializerMethodField()
    #Q16:
    # author = serializers.SlugRelatedField(
    #     slug_field='name',
    #     queryset=Author.objects.all() 
    # )
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_date', 'description']
        #Q14:
        # read_only_fields = ['publication']

    # def create(self, validated_data):
    #     return Book(**validated_data)
    
    #Q15:
    # def get_book_and_author(self, object: Book):
    #     return f'{object.title} by {object.author}'

    #Q10:
    def validate_publication_date(self, publication_year):
        current_date = timezone.now().date()

        if publication_year > current_date:
            raise serializers.ValidationError("Publication date cannot be in the future.")

        return publication_year
    
    #Q11:
    #to update only one field we can use partial update with partial=True. example:
    #serializer_update = BookSerializer(book, data = {'publication_date': '2001-01-01'}, partial=True)

    #Q12:
    #to generate nested representations we can use depth. it should be set to an integer that indicates the depth of relationships that should be traversed before reverting to a flat representation.

    #Q14:
    #read_only_fields are to include additional information in your serialized output without allowing clients to provide values for these fields when creating or updating objects.

    #Q15:
    #SerializerMethodField is a special field used in serializers to include custom, read-only fields in the serialized representation of an object.
    #It allows you to add fields to your serializer that don't directly map to model fields but are derived from the data or involve custom logic.

    #Q16:
    #SlugRelatedField is a serializer field used to represent relationships between objects through a "slug" or a unique identifier instead of the primary key. 
    #when read_only = True on a SlugRelatedField in the serialization The field's value will be included in the serialized data, and it will be based on the value of the related object's field specified by slug_field. 
    #During deserialization: You can't set or update the field when you deserialize data. 

    #Q17:
    #select_related: used for ForeignKey and OneToOneField relationships. It performs a SQL query that follows the relationship and retrieves the related object's fields, all in a single query.
    #example: books = Book.objects.select_related('author')
    #prefetch_related: used for ForeignKey, OneToOneField, and ManyToManyField relationships. performs a separate SQL query for each relationship, retrieves related objects' data, and caches it for use in Python code.
    #typically used for "reverse" relationships, such as accessing objects on the other side of a ForeignKey or ManyToMany relationship.
    #example: authors = Author.objects.prefetch_related('book_set') book_set is the reverse relation for Book.

    #Q18:
    #UserSerializer:
    # class UserSerializer(serializers.ModelSerializer):
    #     messages = MessageSerializer(many=True, read_only=True)

    #     class Meta:
    #         model = User
    #         fields = '__all__'

    #to get all info on user and its messages:
    # class UserView(APIView):
    # def get(self, request, user_id):
    #     user = User.objects.get(id=user_id)
    #     serializer = UserSerializer(user)
    #     return Response(serializer.data)

    #Q19:
    #HyperlinkedRelatedField also allows you to represent a relationship between objects as hyperlinks. It's commonly used when you want to represent related objects in a way that's easily navigable via URLs, and it's particularly useful when creating or updating relationships between objects through the API.