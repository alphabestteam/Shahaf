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

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

@api_view(["GET"])
def get_comment_by_id(request, id):  # to get recipe by id
    comment_id = id
    comment = get_object_or_404(Comment, id=comment_id)
    comment_data = CommentSerializer(comment).data
    return Response(comment_data, status = 200)

@api_view(["DELETE"])
def delete_comment_by_id(request, comment_id, user_id):  # to delete recipe by id
    comment = get_object_or_404(Comment, id=comment_id)
    if comment.user_id == user_id:
        comment.delete()
        return Response("Comment deleted successfully!", status = 200)
    
    else:
        return Response("Cant delete a comment you didn't created!", status = 404)