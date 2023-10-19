from django.urls import path

from . import views

urlpatterns = [
    path("getAllPeople/", views.get_all_people),
    path("addPerson/", views.add_person),
    path("removePerson/<int:id>/", views.remove_person),
    path("updatePerson/", views.update_person),
    # section 5
    path("addParent/", views.add_parent),
    path("removeParent/<int:id>/", views.remove_parent),
    path("updateParent/", views.update_parent),
    path("getAllParents/", views.get_all_parents),
    path("setChildToParent/", views.set_child),
    path("getInformation/<int:id>/", views.get_information),
    path("richChildren/", views.rich_children),
    path("findParents/<int:id>/", views.find_parents),
    path("findParentsSerializer/<int:id>/", views.find_parents_serializer),
    path("informationChildren/<int:id>/", views.information_children),
    path("findGrandparents/<int:id>/", views.find_grandparents),
    path("findSiblings/<int:id>/", views.find_siblings),
    #section 6
    path("infoOnParent", views.info_on_parent),
    path("numberGoogleParents", views.number_google_parents),
    path("orderedParentsByChildBirth", views.ordered_parents_by_child_birth),
    path("nameStartI", views.name_start_i),
    path("tlvOrRaanana", views.tlv_or_raanana),
    path("avgSalary", views.avg_salary),
    path("parentNameChildrenNumber", views.parent_name_children_number),
    path("sumAllChildren", views.sum_all_children),
    path("highestSalary", views.highest_salary),
    path("parentsAvgSalary", views.parents_avg_salary),