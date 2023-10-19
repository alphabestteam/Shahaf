from django.test import TestCase
from .models import Person, Parent
from .views import *

class PersonTestCase(TestCase):
    def setUp(self):
        Person.objects.create(name = 'shahaf', date_of_birth = '2004-10-23', city = 'Netaim', id = '214653602')

    def test_is_18(self):  #checks if person is over 18 if he is return True else False
        person = Person.objects.get(id = '214653602')
        result = person.is_18()
        self.assertEqual(result, True)

    def test_add_parent(self):

    def test_remove_parent(self):

    def test_update_parent(self):

    def test_get_all_parents(self):

    def test_set_child(self):

    def test_get_information(self):

    def test_rich_children(self):

    def test_find_parents(self):

    def test_information_children(self):

    def test_find_siblings(self):