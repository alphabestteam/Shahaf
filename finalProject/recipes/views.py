from django.shortcuts import render
from .models import Recipe
from rest_framework import viewsets
from .serializers import RecipeSerializer
from rest_framework.request import Request
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view, action

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
        asian_recipes = Recipe.objects.filter(type = 'asian').all()
        if len(asian_recipes) > 0:
            asian_serializer = RecipeSerializer(asian_recipes, many=True)
            return Response(asian_serializer.data, status=200)
        else:
            print(asian_recipes)
            return Response(asian_recipes, status=200)
    except:
        return Response('No asian', status=404)
    
@api_view(["GET"])
def get_all_medit(request):  # to get all mediterranean recipes
    try:
        medit_recipes = Recipe.objects.filter(type = 'mediterranean').all()
        if len(medit_recipes) > 0:
            medit_serializer = RecipeSerializer(medit_recipes, many=True)
            return Response(medit_serializer.data, status=200)
        else:
            print(medit_recipes)
            return Response(medit_recipes, status=200)
    except:
        return Response('No mediterranean', status=404)
    
@api_view(["GET"])
def get_all_italian(request):  # to get all italian recipes 
    try:
        italian_recipes = Recipe.objects.filter(type = 'italian').all()
        if len(italian_recipes) > 0:
            italian_serializer = RecipeSerializer(italian_recipes, many=True)
            return Response(italian_serializer.data, status=200)
        else:
            print(italian_recipes)
            return Response(italian_recipes, status=200)
    except:
        return Response('No italian', status=404)
    
@api_view(['GET'])
def get_all_dessert(request):  # to get all dessert recipes
    try:
        dessert_recipes = Recipe.objects.filter(type = 'desserts').all()
        if len(dessert_recipes) > 0:
            dessert_serializer = RecipeSerializer(dessert_recipes, many=True)
            return Response(dessert_serializer.data, status=200)
        else:
            print(dessert_recipes)
            return Response(dessert_recipes, status=200)
    except:
        return Response('No desserts', status=404)
    
@api_view(["GET"])
def get_all_other(request):  # to get all other recipes
    try:
        other_recipes = Recipe.objects.filter(type = 'other').all()
        if len(other_recipes) > 0:
            other_serializer = RecipeSerializer(other_recipes, many=True)
            return Response(other_serializer.data, status=200)
        else:
            print(other_recipes)
            return Response(other_recipes, status=200)
    except:
        return Response('No other', status=404)