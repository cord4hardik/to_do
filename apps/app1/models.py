from django.db import models
from apps.accounts.models import User

# models for todo functionality
class Todo(models.Model):
    STATUS_CHOICES = (
        ('todo', 'To Do'),
        ('in_progress', 'In Progress'),
        ('done', 'Done'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    due_date = models.DateTimeField()
    category = models.CharField(max_length=50)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)


# models for access-log functionality
class AccessLog(models.Model):
    todo = models.ForeignKey(Todo, on_delete=models.CASCADE)
    shared_with = models.ForeignKey(User, on_delete=models.CASCADE, related_name='shared_todos')
    shared_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='shared_by')
    read_only = models.BooleanField(default=False)
    read_write = models.BooleanField(default=False)
    changes_requested = models.BooleanField(default=False)
    approved = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)