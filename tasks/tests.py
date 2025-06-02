from django.test import TestCase
from .models import Task, TaskHistory
from django.contrib.auth.models import User

class TaskModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.task = Task.objects.create(
            name='Test Task',
            description='This is a test task.',
            status='Nowy',
            assigned_user=self.user
        )

    def test_task_creation(self):
        self.assertEqual(self.task.name, 'Test Task')
        self.assertEqual(self.task.description, 'This is a test task.')
        self.assertEqual(self.task.status, 'Nowy')
        self.assertEqual(self.task.assigned_user, self.user)

class TaskHistoryModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.task = Task.objects.create(
            name='Test Task',
            description='This is a test task.',
            status='Nowy',
            assigned_user=self.user
        )
        self.history = TaskHistory.objects.create(
            task=self.task,
            changed_by=self.user,
            changes='{"name": [null, "Test Task"]}'
        )

    def test_task_history_creation(self):
        self.assertEqual(self.history.task, self.task)
        self.assertEqual(self.history.changed_by, self.user)
        self.assertEqual(self.history.changes, '{"name": [null, "Test Task"]}')