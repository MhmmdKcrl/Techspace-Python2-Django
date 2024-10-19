from django.test import TestCase
from core.models import Contact


class TestContactModel(TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.data = {
            'name': 'John Doe',
            'email': 'john@mail.com',
            'subject': 'Hello',
            'message': 'Hello, testttt'
        }
        cls.contact = Contact.objects.create(**cls.data)
        return super().setUpClass()
    

    def test_contact_model(self):
        contact_obj = Contact.objects.get(id=1)
        self.assertEqual(self.contact, contact_obj)
    

    @classmethod
    def tearDownClass(cls) -> None:
        pass

    
