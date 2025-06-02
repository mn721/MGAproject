from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import json

class Task(models.Model):
    status_choices = [
        ("Nowy", "Nowy"),
        ("W toku", "W toku"),
        ("Rozwiązany", "Rozwiązany"),
    ]

    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True, max_length=4000)
    status = models.CharField(
        max_length=20,
        choices=status_choices,
        default="Nowy",
    )
    assigned_user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class TaskHistory(models.Model):
    task = models.ForeignKey(
        Task,
        on_delete=models.CASCADE,
        related_name='history',
    )
    changed_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    changed_at  = models.DateTimeField(default=timezone.now)
    changes  = models.JSONField()

    def __str__(self):
        return f"Historia zmian dla {self.task.name} wykonana {self.changed_at}"