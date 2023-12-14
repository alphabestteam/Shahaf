from django.urls import path, include
from rest_framework.routers import DefaultRouter
from comments.views import CommentViewSet
from . import views

comment_router = DefaultRouter()
comment_router.register(r'', CommentViewSet)

urlpatterns = [
    path('', include(comment_router.urls)),
    path('delete/<int:comment_id>/<int:user_id>/', views.delete_comment_by_id),
]