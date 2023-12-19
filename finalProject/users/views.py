from django.shortcuts import render
from rest_framework import viewsets
from.models import User
from .serializers import UserSerializer
from rest_framework.request import Request
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from recipes.models import Recipe
from recipes.serializers import RecipeSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

@api_view(["GET"])
def get_all_recipes_by_id(request, id):  # to get all recipes
    user_id = id
    user = get_object_or_404(User, id=user_id)
    user_recipes = user.my_recipes.all()
    recipes_serializer = RecipeSerializer(user_recipes, many = True)
    return Response(recipes_serializer.data, status=200)

@api_view(["GET"])
def is_user_exist(request, username):  # check if user exist in db
    user_username = username
    user = get_object_or_404(User, username = user_username)
    return Response(status= 200)

@api_view(["PUT"])
def add_recipe_favorite(request, id_recipe, id_user):  # add a recipe to favorites
    recipe = get_object_or_404(Recipe, recipe_id=id_recipe)
    user = get_object_or_404(User, id = id_user)
    user.my_recipes.add(recipe)
    user_serializer = UserSerializer(user)
    return Response(user_serializer.data, status=200)

@api_view(["PUT"])
def remove_recipe_favorite(request, id_recipe, id_user):  # remove a recipe from  favorites
    recipe = get_object_or_404(Recipe, recipe_id=id_recipe)
    user = get_object_or_404(User, id = id_user)
    user.my_recipes.remove(recipe)
    user_serializer = UserSerializer(user)
    return Response(user_serializer.data, status=200)