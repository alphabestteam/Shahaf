from django.urls import path, include
from rest_framework.routers import DefaultRouter
from forms.views import FormViewSet, ChatFormViewSet, FileFormViewSet
from . import views

form_router = DefaultRouter()
form_router.register(r'forms', FormViewSet)

form_chat_router = DefaultRouter()
form_chat_router.register(r'chat_forms', ChatFormViewSet)

form_file_router = DefaultRouter()
form_file_router.register(r'file_forms', FileFormViewSet)

urlpatterns = [
    path('', include(form_router.urls)),
    path('', include(form_chat_router.urls)),
    path('', include(form_file_router.urls)),
    path('get_status/', views.get_status),
    path('set_user_to_file/', views.set_user_to_file),
]