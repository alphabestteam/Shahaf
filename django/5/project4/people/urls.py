from django.urls import path

from . import views

urlpatterns = [
    path("getAllPeople/", views.get_all_people),
    path("addPerson/", views.add_person),
    path("removePerson/<int:id>/", views.remove_person),
    path("updatePerson/", views.update_person),
    path("addParent/", views.add_parent),
    path("removeParent/<int:id>/", views.remove_parent),
    path("updateParent/", views.update_parent),
    path("getAllParents/", views.get_all_parents),
    path("getInformation/<int:id>/", views.get_information),
    path("richChildren/", views.rich_children),
    path("findParents/<int:id>/", views.find_parents),
]