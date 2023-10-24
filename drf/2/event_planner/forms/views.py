from django.shortcuts import render
from rest_framework import viewsets
from .models import Form, ChatForm, FileForm
from .serializers import FormSerializer, ChatFormSerializer, FileFormSerializer
from rest_framework.request import Request
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from users.models import User

class FormViewSet(viewsets.ModelViewSet):
    queryset = Form.objects.all()
    serializer_class = FormSerializer

class ChatFormViewSet(viewsets.ModelViewSet):
    queryset = ChatForm.objects.all()
    serializer_class = ChatFormSerializer

class FileFormViewSet(viewsets.ModelViewSet):
    queryset = FileForm.objects.all()
    serializer_class = FileFormSerializer

@api_view(['GET'])
def get_status(request, form_id):
    form = get_object_or_404(Form, id = form_id)
    form_data = FormSerializer(Form).data
    status = form_data.status
    return Response(status, status= 200)

@api_view(['POST'])
def set_user_to_file(request): #gets id_form, username
    try:
        data = request.data
        id_form = data['id_form']
        username = data['username']
        form = get_object_or_404(Form, id = id_form)
        user = get_object_or_404(User, username = username)
        if user not in form.users:
            form.users.add(user)
            return Response('user was added to form!', status= 200)
        else:
            return Response('user was already in users of form', status= 404)
    except:
        return Response(status= 404)