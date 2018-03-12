from django.http import HttpRequest
from django.test import TestCase
from django.urls import resolve

from todos.views import todo_list

class TodoListViewTest(TestCase):

    def test_todo_list_resolves(self):
        found = resolve('/todo-list')
        self.assertEqual(found.func, todo_list)

    def test_todo_list_view_has_todo_list_in_html(self):
        request = HttpRequest()
        response = todo_list(request)
        html = response.content.decode('utf8')
        self.assertIn('Todo List', html)
