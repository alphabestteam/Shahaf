from django.urls import path, include
from rest_framework.routers import DefaultRouter
from recipes.views import RecipeViewSet
from . import views

recipe_router = DefaultRouter()
recipe_router.register(r'', RecipeViewSet)

urlpatterns = [
    path('', include(recipe_router.urls)),
    path('get/<int:id>/', views.get_comment_by_id),
    path('delete/<int:comment_id>/<int:user_id>/', views.delete_comment_by_id),
]