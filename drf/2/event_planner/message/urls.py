from django.urls import path, include
from rest_framework.routers import DefaultRouter
from message.views import MessageViewSet

message_router = DefaultRouter()
message_router.register(r'messages', MessageViewSet)

urlpatterns = [
    path('', include(message_router.urls)),
]