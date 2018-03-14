from django.http import HttpRequest
from django.test import TestCase
from django.test import Client
from django.urls import resolve

from main.views import index

client = Client()

class IndexViewTests(TestCase):
    
    def test_index_view_resolves(self):
        found = resolve('/')
        self.assertEqual(found.func, index)

    def test_index_view_has_correct_html(self):
        request = HttpRequest()
        response = index(request)
        html = response.content.decode('utf8')
        self.assertIn('A:', html)
        self.assertIn('B:', html)
        self.assertIn('A + B =', html)

    def test_index_view_generates_two_integers_between_1_and_1000(self):
        response = client.get('/')
        # get context for the page, which is apparently the first thing
        # to show up in a list
        index_context = list(map(lambda x: x, response.context))[0]

        # test that a is less than 1001 and greater than 0
        self.assertLess(index_context['a'], 1001)
        self.assertGreater(index_context['a'], 0)

        # test that b is less than 1001 and greater than 0
        self.assertLess(index_context['b'], 1001)
        self.assertGreater(index_context['b'], 0)
