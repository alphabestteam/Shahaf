from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from targets.models import Target
from targets.serializers import TargetSerializer

@csrf_exempt
def add_target(request):
    if request.method == 'POST':
        request_data = JSONParser().parse(request)
        serializer = TargetSerializer(data =request_data)
        if serializer.is_valid():
            target = TargetSerializer(request_data)
            target.save()
            return JsonResponse(serializer.data, status = 200, safe= False)
        return JsonResponse(serializer.errors, status = 400)

@csrf_exempt
def update_target(request):
    data = JSONParser.parse(request)
    target = Target.objects.get(name = data['target_id'])
    target_serializer = TargetSerializer(data, target)
    if target_serializer.is_valid():
        target.save()
        return JsonResponse('Target was updated!', status = 200)
    
    else:
        return JsonResponse('cant update target, try again!', status = 404)

@csrf_exempt
def all_targets(request):
    if request.method == 'GET':
        targets = Target.objects.all()
        serializer = TargetSerializer(targets, many=True)
        return JsonResponse(serializer.data, safe=False, status=200)