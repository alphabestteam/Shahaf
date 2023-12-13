from django.urls import path, include
from rest_framework.routers import DefaultRouter
from recipes.views import RecipeViewSet
from . import views

recipe_router = DefaultRouter()
recipe_router.register(r'', RecipeViewSet)

urlpatterns = [
    path('', include(recipe_router.urls)),
    path('get/<int:id>/', views.get_recipe_by_id),
    path('update/<int:id>/', views.update_recipe_by_id),
    path('delete/<int:id>/', views.delete_recipe_by_id),
]