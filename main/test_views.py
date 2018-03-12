from django.http import HttpRequest
from django.test import TestCase
from django.urls import resolve

from main.views import index


class SmokeTest(TestCase):

    def test_bad_maths(self):
        self.assertEqual(1 + 1, 2)

class IndexViewTests(TestCase):
    
    def test_index_view_resolves(self):
        found = resolve('/')
        self.assertEqual(found.func, index)

    def test_index_view_has_correct_html(self):
        request = HttpRequest()
        response = index(request)
        html = response.content.decode('utf8')
        self.assertIn('Yeah!', html)

