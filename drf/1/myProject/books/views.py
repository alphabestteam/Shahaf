from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Book
from .serializers import BookSerializer
from django.http import HttpResponse, JsonResponse

def get_all_books(request):
    if request.method == 'GET':
        try:
            queryset = Book.objects.all()
            return HttpResponse(queryset, status = 200)
        
        except:
            return HttpResponse('cant get books', status = 404)

def get_jk_rowling(request):
    if request.method == 'GET':
        try:
            queryset = Book.objects.get(author = 'JK Rowling')
            return HttpResponse(queryset, status = 200)
        
        except:
            return HttpResponse('cant get books', status = 404)