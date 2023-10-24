from django.urls import path, include
from rest_framework.routers import DefaultRouter
from users.views import UserViewSet
from . import views

user_router = DefaultRouter()
user_router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(user_router.urls)),
    path('get_unread_messages/<str:username>/', views.get_unread_messages),
]