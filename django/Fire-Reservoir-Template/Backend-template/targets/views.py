from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser

from targets.models import Target
from targets.serializers import TargetSerializer

@csrf_exempt
def add_target(request):
    # Implement here an add function
    if request.method == 'GET':

    
    elif request.method == 'POST':

@csrf_exempt
def update_target(request):
    # Implement here an update function

def all_targets(request):
    # Implement here a get all targets function
