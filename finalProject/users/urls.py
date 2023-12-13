from django.urls import path, include
from rest_framework.routers import DefaultRouter
from users.views import UserViewSet, UserViewSetByID
from . import views

user_router = DefaultRouter()
user_router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(user_router.urls)),
    path('/get', views.get_user_by_id),
    path('/update', views.update_user_by_id),
    path('/delete', views.delete_user_by_id),
    path('/recipes', views.get_all_recipes_by_id),
    path('/comments', views.get_all_comments_by_id),
    path('/login', views.is_user_exist),
]