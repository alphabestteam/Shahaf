from django.urls import path, include
from rest_framework.routers import DefaultRouter
from users.views import UserViewSet
from . import views

user_router = DefaultRouter()
user_router.register(r'', UserViewSet)

urlpatterns = [
    path('', include(user_router.urls)),
    path('recipes/<int:id>/', views.get_all_recipes_by_id),
    path('login/<str:username>/', views.is_user_exist),
    path('getUser/<str:username>/', views.get_user_username),
    path('addfav/<int:id_recipe>/<int:id_user>/', views.add_recipe_favorite),
    path('removefav/<int:id_recipe>/<int:id_user>/', views.remove_recipe_favorite),
]