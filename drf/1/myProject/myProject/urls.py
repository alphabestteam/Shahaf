"""
URL configuration for myProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from books import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('get_all_books/', views.get_all_books, name='get_all_books'),
    path('get_jk_rowling/', views.get_jk_rowling, name='get_jk_rowling'),
    path('create_book/', views.create_book, name='create_book'),
    path('retrieve_book/', views.retrieve_book, name='retrieve_book'),
    path('update_book/', views.update_book, name='update_book'),
    path('delete_book/', views.delete_book, name='delete_book'),
]
