from django.test import TestCase
from django.urls import reverse
from django.test.client import Client


class TestStatsView(TestCase):

    def setUp(self):

        self.c = Client()

    def test_url(self):

        response = self.c.get(reverse('stats'))
        self.assertEqual(response.status_code, 200)


class TestAuthorView(TestCase):

    def setUp(self):

        self.c = Client()

    def test_url(self):
        req = 'kamilchudy'
        response = self.c.get(reverse('author', args=[req]))
        self.assertEqual(response.status_code, 200)

    def test_url_error(self):
        req = 'somebody'
        response = self.c.get(reverse('author', args=[req]))
        self.assertEqual(response.status_code, 404)
