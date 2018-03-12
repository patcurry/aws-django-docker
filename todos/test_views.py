from django.http import HttpRequest
from django.test import TestCase
from django.urls import resolve

from todos.views import todo_list

class TodoListViewTest(TestCase):

    def test_todo_list_resolves(self):
        found = resolve('/todo-list')
        self.assertEqual(found.func, todo_list)
