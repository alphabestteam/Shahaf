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
def get_recipe_by_id(request, id):  # to get recipe by id
    recipe_id = id
    recipe = get_object_or_404(Recipe, id=recipe_id)
    recipe_data = RecipeSerializer(recipe).data
    return Response(recipe_data, status=200)

@api_view(["PUT"])
def update_recipe_by_id(request, id):  # to update recipe by id
    data = request.data
    recipe = get_object_or_404(Recipe, id = data["id"])
    data_serializer = RecipeSerializer(data)
    recipe_serializer = RecipeSerializer(recipe, data_serializer)
    if recipe_serializer.is_valid():
        recipe_serializer.update(recipe, data)
        return Response("Recipe was updated!", status=200)

    else:
        return Response(recipe_serializer.errors, status=404)

@api_view(["DELETE"])
def delete_recipe_by_id(request, id):  # to delete recipe by id
    recipe_id = id
    recipe = get_object_or_404(Recipe, id = recipe_id)
    recipe.delete()
    return Response("Recipe deleted successfully!", status=200)
