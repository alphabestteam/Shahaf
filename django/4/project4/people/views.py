from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from people.models import Person
from people.serializers import PersonSerializer

@csrf_exempt
def get_all_people(request):
    if request.method == 'GET':
        all_people = Person.objects.all()
        list_of_dict = []
        for one_person in all_people.iterator():
            serializer_person = PersonSerializer('json', one_person)
            if serializer_person.is_valid():
                list_of_dict.append(serializer_person)

            else:
                return JsonResponse(status = 404)
            
        return JsonResponse(list_of_dict, status = 200)


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
            person = Person.objects.get(id)
            person.delete
            return JsonResponse(status = 200)
        
        except:
            return JsonResponse(status = 404)

@csrf_exempt
def update_person(request):
    if request.method == 'POST':
        data = JSONParser.parse(request)
        person = Person.objects.get(name = data['id'])
        person_serializer = PersonSerializer(data, person)
        if person_serializer.is_valid():
            person.save()
            return JsonResponse(status = 200)
        
        else:
            return JsonResponse(status = 404)
