from django.test import TestCase
from core.views import ContactView
from django.urls import reverse_lazy


class TestContactView(TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        return super().setUpClass()

    def test_path(self):
        url = '/en/contact/'
        contact_url = reverse_lazy('core:contact_page')
        self.assertEqual(url, contact_url)

    def test_template(self):
        response = self.client.get('/en/contact/')
        self.assertTemplateUsed(response, 'contact.html')

    def test_status_code(self):
        response = self.client.get('/en/contact/')
        self.assertEqual(response.status_code, 200)

    @classmethod
    def tearDownClass(cls) -> None:
        pass