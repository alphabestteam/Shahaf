from django.shortcuts import render
from rest_framework import viewsets
from .models import Chat
from .serializers import ChatSerializer
from rest_framework.request import Request
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from message.models import Message

class ChatViewSet(viewsets.ModelViewSet):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer

@api_view(['GET'])
def get_all_messages(request, id):
    chat = get_object_or_404(Chat, id = id)
    print(chat)
    chat_data = ChatSerializer(chat).data
    messages = chat.messages
    return Response(messages, status= 200)