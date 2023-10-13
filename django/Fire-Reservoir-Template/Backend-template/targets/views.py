from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser

from targets.models import Target
from targets.serializers import TargetSerializer

@csrf_exempt
def add_target(request):
    data = JSONParser.parse(request)
    data_serializer = TargetSerializer(data)
    if data_serializer.is_valid():
        data_serializer.save()
        return JsonResponse('Target was successfully saved!')
        
    else:
        return JsonResponse('Cant save Target, try again!')

@csrf_exempt
def update_target(request):
    # Implement here an update function
    data = JSONParser.parse(request)
    target = Target.objects.get(name = data['name'])
    target = data
    target.save()
    return JsonResponse('Target was updated!')

def all_targets(request):
    # Implement here a get all targets function
    all_targets = Target.objects.all().values()
    return render(all_targets)
