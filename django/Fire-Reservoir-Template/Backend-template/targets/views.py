from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from targets.models import Target
from targets.serializers import TargetSerializer

@csrf_exempt
def add_target(request):
    # data = JSONParser.parse(request)
    # data_serializer = TargetSerializer(data)
    # if data_serializer.is_valid():
    #     data_serializer.save()
    #     return JsonResponse('Target was successfully saved!', status = 200)
        
    # else:
    #     return JsonResponse('Cant save Target, try again!', status = 404)
    if request.method == 'POST':
        request_data = JSONParser().parse(request)
        target = Target(
            name = request_data["name"],
            attack_priority=request_data["attack_priority"],
            latitude = request_data["latitude"],
            longitude = request_data["longitude"],
            enemy_organization=request_data["enemy_organization"],
            target_goal = request_data["target_goal"],
            is_destroyed = request_data["is_destroyed"],
            target_id = request_data["target_id"]
        )
        serializer = TargetSerializer(data = request_data)
        if serializer.is_valid():
            target.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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
        all_targets = Target.objects.all()
        if not all_targets:
            return JsonResponse({})
        print(len(all_targets))
        target_serializer = TargetSerializer(all_targets)
        return JsonResponse(target_serializer.data, status=200)
