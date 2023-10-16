from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from people.models import Person
from people.serializers import PersonSerializer

@csrf_exempt
def get_all_people(request):

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
            all_people = Person.objects.all()
            
            return JsonResponse(serializer.data, status = 200, safe= False)
        return JsonResponse(serializer.errors, status = 400)

@csrf_exempt
def remove_person(request):

@csrf_exempt
def update_person(request):
