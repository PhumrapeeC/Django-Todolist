from django.test import TestCase, Client
from django.contrib.auth.models import User
from .models import Todo
from django.urls import reverse

class TodoAppTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='tester', password='test1234')
        self.todo = Todo.objects.create(
            user=self.user,
            title='Test Todo',
            description='Test Description',
            status='PENDING'
        )

    def test_signup(self):
        response = self.client.post(reverse('signup'), {
            'username': 'newuser',
            'password1': 'testpass123',
            'password2': 'testpass123'
        })
        self.assertEqual(response.status_code, 302)  # redirected after signup
        self.assertTrue(User.objects.filter(username='newuser').exists())

    def test_login(self):
        response = self.client.post(reverse('login'), {
            'username': 'tester',
            'password': 'test1234'
        })
        self.assertEqual(response.status_code, 302)  # redirected after login

    def test_add_todo(self):
        self.client.login(username='tester', password='test1234')
        response = self.client.post(reverse('add_todo'), {
            'title': 'New Todo',
            'description': 'Description here',
            'status': 'PENDING'
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Todo.objects.filter(title='New Todo').exists())

    def test_display_todo_list(self):
        self.client.login(username='tester', password='test1234')
        response = self.client.get(reverse('todo_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Todo')

    def test_edit_todo(self):
        self.client.login(username='tester', password='test1234')
        response = self.client.post(reverse('edit_todo', args=[self.todo.id]), {
            'title': 'Updated Todo',
            'description': 'Updated',
            'status': 'DONE'
        })
        self.todo.refresh_from_db()
        self.assertEqual(self.todo.title, 'Updated Todo')
        self.assertEqual(self.todo.status, 'DONE')

    def test_delete_todo(self):
        self.client.login(username='tester', password='test1234')
        response = self.client.post(reverse('delete_todo', args=[self.todo.id]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Todo.objects.filter(id=self.todo.id).exists())
