from django.test import TestCase
from .models import Person, Parent

class PersonTestCase(TestCase):
    def setUp(self):
        Person.objects.create(name = 'shahaf', date_of_birth = '2004-10-23', city = 'Netaim', id = '214653602')

    def test_is_18(self):
        person = Person.objects.get(id = '214653602')
        result = person.is_18()
        self.assertEqual(result, True)