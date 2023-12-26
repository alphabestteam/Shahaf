from django.shortcuts import render

from django.shortcuts import render
from .models import Comment
from rest_framework import viewsets
from .serializers import CommentSerializer
from rest_framework.request import Request
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from users.models import User
from recipes.models import Recipe

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def create(self, request, *args, **kwargs):
        comment_serializer = CommentSerializer(data = request.data)
        print(request.data)
        if comment_serializer.is_valid():
            comment_serializer.save()
            return Response(comment_serializer.data, status=200)
        return Response (comment_serializer.errors, status=404)


@api_view(["DELETE"])
def delete_comment_by_id(request, comment_id, username):  # to delete recipe by id
    comment = get_object_or_404(Comment, comment_id=comment_id)
    user = get_object_or_404(User, username = comment.username)
    recipe = get_object_or_404(Recipe, recipe_id = comment.recipe_id.recipe_id)
    recipe.comments_number -= 1
    recipe.sum_stars -= comment.stars
    if user.username == username:
        comment.delete()
        return Response("Comment deleted successfully!", status = 200)
    
    else:
        return Response("Cant delete a comment you didn't created!", status = 404)

# sushi rice Seaweed fillings as you like

# put a thin layer of rice on the seaweed put fillings as you like on one side of the seaweed (not too much) roll tight