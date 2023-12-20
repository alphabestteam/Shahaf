from django.urls import path, include
from rest_framework.routers import DefaultRouter
from recipes.views import RecipeViewSet
from . import views

recipe_router = DefaultRouter()
recipe_router.register(r'', RecipeViewSet)

urlpatterns = [
    path('', include(recipe_router.urls)),
    path('get/<int:id>/', views.get_all_comments_by_id),
    path('getAsian', views.get_all_asian),
    path('getMedit', views.get_all_medit),
    path('getItalian', views.get_all_italian),
    path('getDessert', views.get_all_dessert),
    path('getOther', views.get_all_other),
]