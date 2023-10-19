from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from people.models import Person, Parent
from people.serializers import PersonSerializer, ParentSerializer
import json
from rest_framework import status
from django.db.models import Q, Avg, Count, Sum

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
        parent_serializer = ParentSerializer(parent, data)
        if parent_serializer.is_valid():
            parent_serializer.save()
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
def set_child(request):
    if request.method == 'POST':
        try:
            dict_id = JSONParser().parse(request)
            parent = Parent.objects.get(id = dict_id["parent_id"])
            child = Person.objects.get(id = dict_id["child_id"])
            if child not in parent.children.all():
                parent.children.add(child)
                return HttpResponse('connected child to parent', status = 200)
            
            else:
                return HttpResponse('child already added', status = 404)
        
        except:
            return HttpResponse('error', status = 404)

@csrf_exempt
def get_information(request, id):
    if request.method == 'GET':
        try:
            parent = Parent.objects.get(id = id)
            return HttpResponse(parent, status = 200)

        except:
            return HttpResponse(parent, status = 404)
        
@csrf_exempt
def rich_children(request):
    if request.method == 'GET':
        all_parents = Parent.objects.all()
        list_of_rich = []
        for one_parent in all_parents.all():
            try:
                if one_parent.salary >= 50000.00:
                    children = one_parent.children.all()
                    if children not in list_of_rich:
                        list_of_rich.append(children)

            except:
                return HttpResponse(one_parent.errors, status = 404)
            
        return HttpResponse(list_of_rich, status = 200)
    
@csrf_exempt
def find_parents(request, id):
    if request.method == 'GET':
        all_parents = Parent.objects.all()
        list_of_parents = []
        for one_parent in all_parents.all():
            try:
                for child in one_parent.children.all():
                    if int(child.id) == int(id):
                        list_of_parents.append(one_parent)

            except:
                return HttpResponse(one_parent, status = 404)
            
        return HttpResponse(list_of_parents, status = 200)
    
@csrf_exempt
def find_parents_serializer(request, id): 
    if request.method == 'GET':
        try:
            person = Person.objects.get(id = id)
            parents = person.parents.all()
            serializer = ParentSerializer(parents)
            return HttpResponse(parents, status = 200)
        
        except:
            return HttpResponse(status = 404)
    
@csrf_exempt
def information_children(request, id):
    if request.method == 'GET':
        try:
            parent = Parent.objects.get(id = id)
            children = parent.children.all()
            return HttpResponse(children, status = 200)
            
        except:
            return HttpResponse('cant find parent', status = 404)
        
@csrf_exempt
def find_grandparents(request, id):
    if request.method == 'GET':
        try:
            person = Person.objects.get(id = id)
            all_parents = person.parents.all()
            grandparents = []
            for parent in all_parents:
                grandparents.append(parent.parents.all())

            return HttpResponse(grandparents, status = 200)

        except:
            return HttpResponse(grandparents, status = 404)

@csrf_exempt
def find_siblings(request, id):
    if request.method == 'GET':
        try:
            person = Person.objects.get(id = id)
            parent = person.parents.first()
            siblings = parent.children.all()
            return HttpResponse(siblings, status = 200)

        except:
            return HttpResponse(status = 404)

#6 section
        
@csrf_exempt
def info_on_parent(request):
    if request.method == 'GET':
        try:
            parents_info = Parent.objects.all().values()
            return HttpResponse(parents_info, status = 200)
        
        except:
            return HttpResponse(status = 400)

@csrf_exempt
def number_google_parents(request):
    if request.method == 'GET':
        try:
            google_parents = Parent.objects.filter(Q(place_of_work = 'Google')| Q(place_of_work = 'google')).count()
            return HttpResponse(f'The number of parents working in google is: {google_parents}', status = 200)
        except:
            return HttpResponse('query failed', status = 404)

@csrf_exempt
def ordered_parents_by_child_birth(request):  #fix
    if request.method == 'GET':
        try:
            parents = Parent.objects.filter(children__isnull = False).order_by('children__date_of_birth')
            return HttpResponse(parents, status = 200)

        except:
            return HttpResponse(status = 404)

@csrf_exempt
def name_start_i(request):
    if request.method == 'GET':
        try:
            people_with_i_names = Person.objects.filter(Q(name__startswith='I')| Q(name__startswith='i'))
            return HttpResponse(people_with_i_names, status = 200)

        except:
            return HttpResponse('cant find people', status = 404)

@csrf_exempt
def tlv_or_raanana(request):
    if request.method == 'GET':
        try:
            tlv_or_raanana = Person.objects.filter(Q(city='Tel Aviv')| Q(name__startswith='Raanana')| Q(city='tel aviv')| Q(name__startswith='raanana'))
            return HttpResponse(tlv_or_raanana, status = 200)

        except:
            return HttpResponse('cant find people', status = 404)

@csrf_exempt
def avg_salary(request):
    if request.method == 'GET':
        try:
            avg = Parent.objects.aggregate(avg_salary_parent = Avg('salary'))
            return HttpResponse(avg, status = 200)

        except:
            return HttpResponse('cant find avg', status = 404)

@csrf_exempt
def parent_name_children_number(request):
    if request.method == 'GET':
        try:
            parents_with_children_count = Parent.objects.annotate(num_children = Count('children'))
            return HttpResponse([{'name': parent.name, 'num_children': parent.num_children} for parent in parents_with_children_count], status = 200)

        except:
            return HttpResponse('error', status = 404)

@csrf_exempt
def sum_all_children(request):
    if request.method == 'GET':
        try:
            all_children = Parent.objects.annotate(sum_children = Sum('children')).count()
            return HttpResponse(all_children, status = 200)

        except:
            return HttpResponse('error', status = 404)

@csrf_exempt
def highest_salary(request):
    if request.method == 'GET':
        try:
            highest_salary_parent = Parent.objects.all().order_by('salary').first()
            return HttpResponse(highest_salary_parent, status = 200)
        
        except:
            return HttpResponse('error', status = 200)

@csrf_exempt
def parents_avg_salary(request):
    if request.method == 'GET':
        try:
            parents_avg = Person.objects.annotate(avg_parent_salary = Avg('parents__salary')).filter(avg_parent_salary__gte=50000)
            return HttpResponse(parents_avg, status = 200)
        
        except:
            return HttpResponse('error', status = 200)