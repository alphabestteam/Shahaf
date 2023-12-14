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
    recipe = get_object_or_404(Recipe, recipe_id=id)
    recipe_comments = RecipeSerializer(recipe).data.comments
    return Response(recipe_comments, status=200)

#update comments when comment created

#update avg when comment created