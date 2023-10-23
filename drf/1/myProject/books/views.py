from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Book
from rest_framework import status
from rest_framework.decorators import api_view
from .serializers import BookSerializer
from django.http import HttpResponse, JsonResponse
from rest_framework.request import Request
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt


# Q1:
def get_all_books(request):
    if request.method == "GET":
        try:
            queryset = Book.objects.all()
            return HttpResponse(queryset, status=200)

        except:
            return HttpResponse("cant get books", status=404)


def get_jk_rowling(request):
    if request.method == "GET":
        try:
            queryset = Book.objects.get(author="JK Rowling")
            return HttpResponse(queryset, status=200)

        except:
            return HttpResponse("cant get books", status=404)


# Q2:
# .data returns the parsed content of the request.


@api_view(["POST"])
def create_book(request):
    request_data = request.data
    serializer = BookSerializer(data=request_data)
    if serializer.is_valid():
        serializer.save()
        return Response(request_data, status=status.HTTP_201_CREATED)

    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET"])
def retrieve_book(request):
    name = request.query_params.get("title")
    book = get_object_or_404(Book, title=name)
    book_data = BookSerializer(book).data
    return Response(book_data, status=200)


@api_view(["POST"])
def update_book(request):
    data = request.data
    book = get_object_or_404(Book, title = data["title"])
    book_serializer = BookSerializer(book, data)
    if book_serializer.is_valid():
        book_serializer.update(book, data)
        return Response("Book was updated!", status=200)

    else:
        return Response(book_serializer.errors, status=404)


@api_view(["DELETE"])
def delete_book(request, name):
    print(name)
    book = get_object_or_404(Book, title = name)
    book.delete()
    return Response("deleted", status=200)


# Q3:
# query params is like request.GET but better. It is a dictionary-like object that allows us to access the query parameters sent with the URL as part of an HTTP request.

# Q4:
# the difference between Response() and HttpResponse() is that unlike HttpResponse objects, you dont instantiate Response objects with rendered content.

# Q5:
# class-based-views : drf provides an APIView class which subclasses Django view class.
# Request instances will be passed to the handler and not HttpRequest instances.
# the handler will return Response and not HttpResponse. 

# function-based-views : provides a set of simple decorators that wrap your function based views to ensure they receive an instance of Request.
# and allows them to return a Response.


class BookCRUD(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAdminUser]

    @csrf_exempt
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    @csrf_exempt
    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @csrf_exempt
    def delete(self, request, title):
        book = self.get_object_or_404(Book, title=title)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @csrf_exempt
    def put(self, request, title):
        book = self.get_object_or_404(Book, title=title)
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Q6:
# to make a function based view include a couple of http methods we can put in the decorator all the http methods we want to use for example @api_view(['GET', 'POST']).

# Q7:
# When you call the save() method on a new instance, Django generates a new primary key value for it and inserts a new record into the database. It effectively creates a new object.
# If you modify any fields of the retrieved object and then call the save() method, Django knows to update the existing record in the database rather than creating a new one.

# Q8:
# we can print the validation error by returning the serializer_data.error

# Q9:
# this line checks if the serializer data is valid and if it is it continues and if not it raises an exception.
