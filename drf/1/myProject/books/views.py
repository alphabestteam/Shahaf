from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Book
from rest_framework import status
from rest_framework.decorators import api_view
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

# .data returns the parsed content of the request.
@api_view(['POST'])
def create_book(request):
    if request.method == 'POST':
        request_data = request.data
        serializer = BookSerializer(data = request_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status = status.status.HTTP_201_CREATED, safe= False)
        return JsonResponse(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

def retrieve_book(request, name):
    if request.method == 'GET':
        try:
            book = Book.objects.get(title = name)
            return JsonResponse(book.data, status = 200, safe= False)
        except:
            return JsonResponse(book.errors, status = 400)

def update_book(request):
    if request.method == 'POST':
        data = request.data
        book = Book.objects.get(id = data['id'])
        book_serializer = BookSerializer(book, data)
        if book_serializer.is_valid():
            data.save()
            return JsonResponse(book_serializer.data, status = 200)
        
        else:
            return JsonResponse(book_serializer.errors, status = 404)

def delete_book(request, name):
    if request.method == 'DELETE':
        try:
            book = Book.objects.get(title = name)
            book.delete()
            return HttpResponse('deleted', status = 200)
            
        except:
            return HttpResponse('error', status = 404)