from django.urls import path, include
from rest_framework.routers import DefaultRouter
from chats.views import ChatViewSet
from . import views

chat_router = DefaultRouter()
chat_router.register(r'chats', ChatViewSet)

urlpatterns = [
    path('', include(chat_router.urls)),
    path('get_all_messages/<str:id>/', views.get_all_messages),
]