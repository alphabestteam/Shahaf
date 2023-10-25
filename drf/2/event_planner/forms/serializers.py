from rest_framework import serializers
from .models import Form, ChatForm, FileForm

class FormSerializer(serializers.ModelSerializer):
    class Meta:
        model = Form
        fields = '__all__'

class ChatFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatForm
        fields = '__all__'

class FileFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileForm
        fields = '__all__'