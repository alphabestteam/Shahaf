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

    def test_remove_parent(self):  #return error
        parent_id = '214653602'  
        url = reverse('remove_parent', args=[parent_id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_parent(self):  #return error (person not found)
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

    # def test_get_all_parents(self):

    # def test_set_child(self):

    # def test_get_information(self):

    # def test_rich_children(self):

    # def test_find_parents(self):

    # def test_information_children(self):

    # def test_find_siblings(self):