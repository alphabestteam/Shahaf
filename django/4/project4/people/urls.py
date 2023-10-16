from django.urls import path

from . import views

urlpatterns = [
    path("getAllPeople/", views.get_all_people),
    path("addPerson/", views.add_person),
    path("removePerson/<int:id>/", views.remove_person),
    path("updatePerson/", views.update_person),
]