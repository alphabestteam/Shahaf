from django.urls import path, include
from rest_framework.routers import DefaultRouter
from users.views import UserViewSet
from . import views

user_router = DefaultRouter()
user_router.register(r'', UserViewSet)

urlpatterns = [
    path('', include(user_router.urls)),
    path('get/<int:id>/', views.get_user_by_id),
    path('update/<int:id>/', views.update_user_by_id),
    path('delete/<int:id>/', views.delete_user_by_id),
    path('recipes/<int:id>/', views.get_all_recipes_by_id),
    path('comments/<int:id>/', views.get_all_comments_by_id),
    path('login/<int:id>/', views.is_user_exist),
]