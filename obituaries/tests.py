from django.test import TestCase
from django.urls import reverse
from .models import Obituary

class ObituaryTests(TestCase):
    def setUp(self):
        self.obituary = Obituary.objects.create(
            name="John Doe",
            date_of_birth="1950-01-01",
            date_of_death="2023-01-01",
            content="Test obituary content",
            author="Test Author"
        )

    def test_obituary_creation(self):
        self.assertTrue(isinstance(self.obituary, Obituary))
        self.assertEqual(self.obituary.__str__(), self.obituary.name)

    def test_view_obituaries(self):
        url = reverse('view_obituaries')
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        self.assertIn(self.obituary.name, str(resp.content))

    def test_obituary_form(self):
        url = reverse('obituary_form')
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
