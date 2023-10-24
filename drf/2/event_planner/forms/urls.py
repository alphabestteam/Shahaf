from django.urls import path, include
from rest_framework.routers import DefaultRouter
from forms.views import FormViewSet, ChatFormViewSet, FileFormViewSet

form_router = DefaultRouter()
form_router.register(r'forms', FormViewSet)

form_chat_router = DefaultRouter()
form_chat_router.register(r'forms', ChatFormViewSet)

form_file_router = DefaultRouter()
form_file_router.register(r'forms', FileFormViewSet)

urlpatterns = [
    path('', include(form_router.urls)),
    path('', include(form_chat_router.urls)),
    path('', include(form_file_router.urls)),
]