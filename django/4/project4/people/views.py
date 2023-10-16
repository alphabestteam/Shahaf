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

@csrf_exempt
def remove_person(request):

@csrf_exempt
def update_person(request):
