from django.shortcuts import render
from .models import Recipe
from rest_framework import viewsets
from .serializers import RecipeSerializer
from rest_framework.request import Request
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view

class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

@api_view(["GET"])
def get_all_comments_by_id(request, id):  # to get all comments
    recipe = get_object_or_404(Recipe, recipe_id = id)
    recipe_comments = recipe.recipe_comments
    return Response(recipe_comments, status=200)

@api_view(["GET"])
def get_all_asian(request):  # to get all asian recipes
    try:
        asian_recipes = Recipe.objects.filter(type = 'asian')
        return Response(asian_recipes, status=200)
    except:
        return Response(asian_recipes.error, status=404)
    
@api_view(["GET"])
def get_all_medit(request):  # to get all mediterranean recipes
    try:
        medit_recipes = Recipe.objects.filter(type = 'mediterranean')
        return Response(medit_recipes, status=200)
    except:
        return Response(medit_recipes.error, status=404)
    
@api_view(["GET"])
def get_all_italian(request):  # to get all italian recipes
    try:
        italian_recipes = Recipe.objects.filter(type = 'italian')
        return Response(italian_recipes, status=200)
    except:
        return Response(italian_recipes.error, status=404)
    
@api_view(["GET"])
def get_all_dessert(request):  # to get all dessert recipes
    try:
        dessert_recipes = Recipe.objects.filter(type = 'dessert')
        return Response(dessert_recipes, status=200)
    except:
        return Response(dessert_recipes.error, status=404)
    
@api_view(["GET"])
def get_all_other(request):  # to get all other recipes
    try:
        other_recipes = Recipe.objects.filter(type = 'other')
        return Response(other_recipes, status=200)
    except:
        return Response(other_recipes.error, status=404)