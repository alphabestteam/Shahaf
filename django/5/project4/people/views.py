from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from people.models import Person, Parent
from people.serializers import PersonSerializer, ParentSerializer
import json
from rest_framework import status

@csrf_exempt
def get_all_people(request):
    if request.method == 'GET':
        all_people = Person.objects.all()
        list_of_dict = []
        for one_person in all_people.iterator():
            try:
                one_person = one_person.__dict__
                list_of_dict.append(one_person)

            except:
                return HttpResponse(one_person.errors, status = 404)
            
        return HttpResponse(list_of_dict, status = 200)


@csrf_exempt
def add_person(request):
    if request.method == 'POST':
        request_data = JSONParser().parse(request)
        person = Person(
            name = request_data["name"],
            date_of_birth = request_data["date_of_birth"],
            city = request_data["city"],
            id = request_data["id"]
        )
        serializer = PersonSerializer(data = request_data)
        if serializer.is_valid():
            person.save()
            return JsonResponse(serializer.data, status = 200, safe= False)
        return JsonResponse(serializer.errors, status = 400)

@csrf_exempt
def remove_person(request, id):
    if request.method == 'DELETE':
        try:
            person = Person.objects.get(id = id)
            person.delete()
            return HttpResponse('deleted', status = 200)
            
        except:
            return HttpResponse('error', status = 404)

@csrf_exempt
def update_person(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        person = Person.objects.get(id = data['id'])
        print(person)
        person_serializer = PersonSerializer(person, data)
        if person_serializer.is_valid():
            person_serializer.update(person, data)
            return JsonResponse(person_serializer.data, status = 200)
        
        else:
            return JsonResponse(person_serializer.errors, status = 404)

#5 section

@csrf_exempt
def add_parent(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ParentSerializer(data=data)
        if serializer.is_valid():
            parent = parent = Parent(name = data['name'], date_of_birth = data['date_of_birth'], city = data['city'], id = data['id'], place_of_work = data['place_of_work'], salary = data['salary'])
            parent.save()
            parent.children.set(data.get('children', []))
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
def remove_parent(request, id):
    if request.method == 'DELETE':
        try:
            parent = Parent.objects.get(id = id)
            parent.delete()
            return HttpResponse('deleted', status=status.HTTP_204_NO_CONTENT)
            
        except:
            return HttpResponse('error', status=status.HTTP_404_NOT_FOUND)

@csrf_exempt
def update_parent(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        parent = Parent.objects.get(id = data['id'])
        print(parent)
        parent_serializer = ParentSerializer(parent, data)
        if parent_serializer.is_valid():
            parent_serializer.update()
            return JsonResponse(parent_serializer.data, status = 200)
        
        else:
            return JsonResponse(parent_serializer.errors, status = 404)

@csrf_exempt
def get_all_parents(request):
    if request.method == 'GET':
        all_parents = Parent.objects.all()
        list_of_dict = []
        for one_parent in all_parents.iterator():
            try:
                one_parent = one_parent.__dict__
                list_of_dict.append(one_parent)

            except:
                return HttpResponse(one_parent.errors, status = 404)
            
        return HttpResponse(list_of_dict, status = 200)
    
@csrf_exempt
def get_information(request, id):
    if request.method == 'GET':
        try:
            parent = Parent.objects.get(id = id)
            return JsonResponse(parent.data, status = 200)

        except:
            return JsonResponse(parent.errors, status = 404)
        
@csrf_exempt
def rich_children(request):
    if request.method == 'GET':
        all_parents = Parent.objects.all()
        list_of_rich = []
        for one_parent in all_parents.iterator():
            try:
                if one_parent.salary >= 50000.00:
                    list_of_rich.append(one_parent.children)

            except:
                return HttpResponse(one_parent.errors, status = 404)
            
        return HttpResponse(list_of_rich, status = 200)
    
@csrf_exempt
def find_parents(request, id):
    if request.method == 'GET':
        all_parents = Parent.objects.all()
        list_of_parents = []
        for one_parent in all_parents.iterator():
            try:
                if one_parent.children.id == id:
                    list_of_parents.append(one_parent)

            except:
                return HttpResponse(one_parent.errors, status = 404)
            
        return HttpResponse(list_of_parents, status = 200)
    
@csrf_exempt
def find_parents_serializer(request, id):  #fix
    if request.method == 'GET':
        all_parents = Parent.objects.all()
        list_of_parents = []
        for one_parent in all_parents.iterator():
            try:
                if ParentSerializer.parent_by_id(id, one_parent):
                    list_of_parents.append(one_parent)

            except:
                return HttpResponse(one_parent.errors, status = 404)
            
        return HttpResponse(list_of_parents, status = 200)
    
@csrf_exempt
def information_children(request, id):
    if request.method == 'GET':
        try:
            parent = Parent.objects.get(id = id)
            return JsonResponse(parent.children, status = 200)
            
        except:
            return HttpResponse(parent.errors, status = 404)
        
@csrf_exempt
def find_grandparents(request, id):
    if request.method == 'GET':
        try:
            person = Person.objects.get(id = id)
            grandparents = person.parents.parents
            return JsonResponse(grandparents.data, status = 200)
        
        except:
            return JsonResponse(grandparents.errors, status = 404)

@csrf_exempt
def find_siblings(request, id):
    if request.method == 'GET':
        try:
            parent = Parent.objects.filter(parent.children.id == id).first()
            siblings = parent.children
            return JsonResponse(siblings.data, status = 200)

        except:
            return JsonResponse(siblings.errors, status = 404)