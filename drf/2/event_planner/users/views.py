from django.shortcuts import render
from rest_framework import viewsets
from .models import User
from .serializers import UserSerializer
from rest_framework.request import Request
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

@api_view(["GET"])
def get_unread_messages(request, username):  # to get all unread messages
    user = get_object_or_404(User, username = username)
    user_data = UserSerializer(user).data
    unread_messages = user_data['unread_messages']
    return Response(unread_messages, status= 200)