from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Book
from rest_framework import status
from rest_framework.decorators import api_view
from .serializers import BookSerializer
from django.http import HttpResponse, JsonResponse
from rest_framework.request import Request

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
        serializer = BookSerializer(data =request_data)
        if serializer.is_valid():
            target = BookSerializer(request_data)
            target.save()
            return JsonResponse(serializer.data, status = 200, safe= False)
        return JsonResponse(serializer.errors, status = 400)

@api_view(['GET'])
def retrieve_book(request):
    if request.method == 'GET':
        try:
            drf_request = Request(request)
            name = drf_request.query_params.get('title')
            book = Book.objects.get(title = name)
            return JsonResponse(book.data, status = 200, safe= False)
        except:
            return JsonResponse(book.errors, status = 400)

@api_view(['POST'])
def update_book(request):
    if request.method == 'POST':
        data = request.data
        book = Book.objects.get(name = data['title'])
        book_serializer = BookSerializer(data, book)
        if book_serializer.is_valid():
            book.save()
            return JsonResponse('Book was updated!', status = 200)
        
        else:
            return JsonResponse('cant update book, try again!', status = 404)

@api_view(['DELETE'])
def delete_book(request, name):
    if request.method == 'DELETE':
        try:
            book = Book.objects.get(title = name)
            book.delete()
            return HttpResponse('deleted', status = 200)
            
        except:
            return HttpResponse('error', status = 404)
        
#query params is a more correct name for request.GET. IT is a dictionary-like object that allows you to access the query parameters sent with a URL as part of an HTTP request.