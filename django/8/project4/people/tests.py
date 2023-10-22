from django.test import TestCase
from .models import Person, Parent
from .views import *
from django.urls import reverse
from rest_framework.test import APIRequestFactory
from rest_framework.parsers import JSONParser
from rest_framework import status
from django.http import JsonResponse
from .serializers import ParentSerializer


class PersonTestCase(TestCase):
    def setUp(self):
        Person.objects.create(name = 'shahaf', date_of_birth = '2004-10-23', city = 'Netaim', id = '214653602')

    def test_is_18(self):  #checks if person is over 18 if he is return True else False
        person = Person.objects.get(id = '214653602')
        result = person.is_18()
        self.assertEqual(result, True)

    def test_add_parent(self):
        factory = APIRequestFactory()
        url = reverse("add_parent") 

        data = {
            'name': 'John',
            'date_of_birth': '1990-01-15',
            'city': 'New York',
            'id': '123456789',
            'place_of_work': 'Company X',
            'salary': 75000.0,
            'children': []  
        }
        data_json = json.dumps(data)
        request = factory.post(url, data_json, content_type='application/json')
        response = add_parent(request)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        data = json.loads(response.content.decode('utf-8'))

        self.assertEqual(data['name'], 'John')
        self.assertEqual(data['date_of_birth'], '1990-01-15')
        self.assertEqual(data['city'], 'New York')
        self.assertEqual(data['id'], '123456789')
        self.assertEqual(data['place_of_work'], 'Company X')
        self.assertEqual(data['salary'], 75000.0)

    def test_remove_parent(self):  #return error
        parent_id = '214653602'  
        url = reverse('remove_parent', args=[parent_id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

        self.assertEqual(response.content, b'error')

    def test_update_parent(self):  
        factory = APIRequestFactory()
        url = reverse("update_parent") 
        parent = Parent.objects.create(
            name= 'John',
            date_of_birth= '1990-01-15',
            city= 'New York',
            id= '123456789',
            place_of_work= 'Company X',
            salary= 75000.0,
            )
        data = {
            'name': 'Matan',
            'date_of_birth': '1990-01-15',
            'city': 'New York',
            'id': '123456789',
            'place_of_work': 'Company X',
            'salary': 95000.0,
            'children': []  
        }
        data_json = json.dumps(data)
        request = factory.post(url, data_json, content_type='application/json')
        response = update_parent(request)

        self.assertEqual(response.status_code, 200)

        data = json.loads(response.content.decode('utf-8'))

        self.assertEqual(data['name'], 'Matan')
        self.assertEqual(data['date_of_birth'], '1990-01-15')
        self.assertEqual(data['city'], 'New York')
        self.assertEqual(data['id'], '123456789')
        self.assertEqual(data['place_of_work'], 'Company X')
        self.assertEqual(data['salary'], 95000.0)

    def test_get_all_parents(self):
        factory = APIRequestFactory()
        url = reverse("get_all_parents") 
        request = factory.get(url, content_type='application/json')
        response = get_all_parents(request)

        self.assertEqual(response.status_code, 200)

    def test_set_child(self):  #sets child to parent
        factory = APIRequestFactory()
        url = reverse("set_child")
        child = Person.objects.create(
            name = 'Agam',
            date_of_birth = '2004-01-15',
            city = 'New York',
            id = '1111'
        )
        parent = Parent.objects.create(
            name= 'John',
            date_of_birth= '1990-01-15',
            city= 'New York',
            id= '123456789',
            place_of_work= 'Company X',
            salary= 75000.0,
            )
        data_json = json.dumps({'parent_id': '123456789', 'child_id': '1111'})
        request = factory.post(url, data_json, content_type='application/json')
        response = set_child(request)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b'connected child to parent')

    def test_get_information(self):  #gets info on parent
        factory = APIRequestFactory()
        url = reverse("get_info", args=['123456789'])
        parent = Parent.objects.create(
            name= 'John',
            date_of_birth= '1990-01-15',
            city= 'New York',
            id= '123456789',
            place_of_work= 'Company X',
            salary= 75000.0,
            )
        request = factory.get(url)
        response = get_information(request, id = parent.id)

        self.assertEqual(response.status_code, 200)
        data = response.content.decode('utf-8')

        self.assertEqual(data, 'parent info: name: John date of birth: 1990-01-15 city: New York id: 123456789 place of work: Company X salary: 75000 with children: <QuerySet []>')

    def test_rich_children(self): #finds rich children ( no rich children )
        factory = APIRequestFactory()
        url = reverse('rich_children')
        request = factory.get(url)
        response = rich_children(request)
        data = response.content.decode('utf-8')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data, '')

    def test_find_parents(self): #finds parents (has no parents)
        factory = APIRequestFactory()
        url = reverse('find_parents', args=['1111'])
        child = Person.objects.create(
            name = 'Agam',
            date_of_birth = '2004-01-15',
            city = 'New York',
            id = '1111'
        )
        request = factory.get(url)
        response = find_parents(request, id = child.id)
        data = response.content.decode('utf-8')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data, '')

    def test_information_children(self): #gets info on children (has no children)
        factory = APIRequestFactory()
        url = reverse('info_children', args=['123456789'])
        parent = Parent.objects.create(
            name= 'John',
            date_of_birth= '1990-01-15',
            city= 'New York',
            id= '123456789',
            place_of_work= 'Company X',
            salary= 75000.0,
            )
        request = factory.get(url)
        response = find_parents(request, id = parent.id)
        data = response.content.decode('utf-8')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data, '')


    def test_find_siblings(self):  #return error (no siblings found)
        factory = APIRequestFactory()
        url = reverse('find_siblings', args=['1111'])
        child = Person.objects.create(
            name = 'Agam',
            date_of_birth = '2004-01-15',
            city = 'New York',
            id = '1111'
        )
        request = factory.get(url)
        response = find_siblings(request, id = child.id)

        self.assertEqual(response.status_code, 404)