from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from people.models import Person
from people.serializers import PersonSerializer
import json

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
            person.delete
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
            person_serializer.save()
            return JsonResponse(person_serializer.data, status = 200)
        
        else:
            return JsonResponse(person_serializer.errors, status = 404)
