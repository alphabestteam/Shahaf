from django.shortcuts import render
from rest_framework import viewsets
from .models import Message
from users.models import User
from chats.views import *
from .serializers import MessageSerializer
from rest_framework.request import Request
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    def create(self, request):
        data = request.data
        serializer = MessageSerializer(data = data)
        chat = request.data.get('chat_pointer')
        is_exist = Chat.objects.filter(id = chat).exists()
        if not is_exist:
            chat_serializer = ChatSerializer(data = {'id': chat})
            if chat_serializer.is_valid():
                chat_serializer.save()
        if serializer.is_valid():
            serializer.save()
            return Response(status = status.HTTP_201_CREATED)


@api_view(['POST'])
def set_message_to_user(request): #gets id_message, username
    try:
        data = request.data
        id_message = data['id_message']
        username = data['username']
        message = get_object_or_404(Message, id = id_message)
        user = get_object_or_404(User, username = username)
        if message.is_read == False:
            user.unread_messages.add(message)
            return Response('message was added!', status= 200)
        else:
            return Response('message was already read or is already in unread messages', status= 404)
    except:
        return Response(status= 404)
