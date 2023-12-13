from django.shortcuts import render
from rest_framework import viewsets
from.models import User
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
def get_user_by_id(request):  # to get user by id
    user_id = request.query_params.get("id")
    user = get_object_or_404(User, id=user_id)
    user_data = UserSerializer(user).data
    return Response(user_data, status=200)

@api_view(["PUT"])
def update_user_by_id(request):  # to update user by id
    data = request.data
    user = get_object_or_404(User, id = data["id"])
    user_serializer = UserSerializer(user, data)
    if user_serializer.is_valid():
        user_serializer.update(user, data)
        return Response("User was updated!", status=200)

    else:
        return Response(user_serializer.errors, status=404)

@api_view(["DELETE"])
def delete_user_by_id(request):  # to delete user by id
    user_id = request.query_params.get("id")
    user = get_object_or_404(User, id = user_id)
    user.delete()
    return Response("User deleted successfully!", status=200)

@api_view(["GET"])
def get_all_recipes_by_id(request, id):  # to get all recipes
    user_id = request.query_params.get("id")
    user = get_object_or_404(User, id=user_id)
    user_recipes = UserSerializer(user).data.recipes
    return Response(user_recipes, status=200)

@api_view(["GET"])
def get_all_comments_by_id(request, id):  # to get all comments
    user_id = request.query_params.get("id")
    user = get_object_or_404(User, id=user_id)
    user_comments = UserSerializer(user).data.comments
    return Response(user_comments, status=200)

@api_view(["GET"])
def is_user_exist(request):  # check if user exist in db
    user_id = request.query_params.get("id")
    user = get_object_or_404(User, id=user_id)
    return Response(status= 200)