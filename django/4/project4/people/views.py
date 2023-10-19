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
        try:
            all_people = Person.objects.all()
            list_of_dict = PersonSerializer(all_people, many = True)
            return HttpResponse(list_of_dict.data, status = 200)
        except:
            return HttpResponse(status = 404)


@csrf_exempt
def add_person(request):
    if request.method == 'POST':
        request_data = JSONParser().parse(request)
        serializer = PersonSerializer(data = request_data)
        if serializer.is_valid():
            person = PersonSerializer(request_data)
            person.save()
            return JsonResponse(serializer.data, status = 200, safe= False)
        return JsonResponse(serializer.errors, status = 400)

@csrf_exempt
def remove_person(request, id):
    if request.method == 'DELETE':
        try:
            person = Person.objects.get(id = id)

        except:
            return HttpResponse('no such person', status = 404)
        
        try:
            person.delete()
            return HttpResponse('deleted', status = 200)
            
        except:
            return HttpResponse('error', status = 404)

@csrf_exempt
def update_person(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        try:
            person = Person.objects.get(id = data['id'])
        except:
            return HttpResponse('no such person', status = 404)
        person_serializer = PersonSerializer(data = data)
        if person_serializer.is_valid():
            person.update(person, data)
            return HttpResponse(person, status = 200)
        
        else:
            return HttpResponse(person, status = 404)
