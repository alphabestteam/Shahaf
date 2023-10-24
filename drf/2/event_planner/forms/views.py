from django.shortcuts import render
from rest_framework import viewsets
from .models import Form, ChatForm, FileForm
from .serializers import FormSerializer, ChatFormSerializer, FileFormSerializer

class FormViewSet(viewsets.ModelViewSet):
    queryset = Form.objects.all()
    serializer_class = FormSerializer

class ChatFormViewSet(viewsets.ModelViewSet):
    queryset = ChatForm.objects.all()
    serializer_class = ChatFormSerializer

class FileFormViewSet(viewsets.ModelViewSet):
    queryset = FileForm.objects.all()
    serializer_class = FileFormSerializer