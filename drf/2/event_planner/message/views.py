from django.shortcuts import render
from rest_framework import viewsets
from .models import Message
from users.models import User
from .serializers import MessageSerializer
from rest_framework.request import Request
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

@api_view(['POST'])
def set_message_to_user(request): #gets query params: id_message, username
    try:
        id_message = request.query_params.get('id_message')
        username = request.query_params.get('username')
        message = get_object_or_404(Message, id = id_message)
        user = get_object_or_404(User, username = username)
        if message.is_read == False and message not in user.unread_messages:
            user.unread_messages.add(message)
            return Response('message was added!', status= 200)
        else:
            return Response('message was already read or is already in unread messages', status= 404)
    except:
        return Response(status= 404)
