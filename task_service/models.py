from django.contrib.auth.models import AbstractUser
from django.db import models


class TaskType(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Position(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Worker(AbstractUser):
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    groups = models.ManyToManyField("auth.Group", related_name="workers")
    user_permissions = models.ManyToManyField("auth.Permission", related_name="workers")

    def __str__(self):
        return self.username


class Task(models.Model):
    PRIORITY_CHOICES = [
        ("immediately", "F"),
        ("low", "D"),
        ("medium", "C"),
        ("high", "B"),
        ("urgent", "A"),
    ]

    name = models.CharField(max_length=255)
    description = models.CharField(max_length=511)
    deadline = models.DateTimeField()
    is_completed = models.BooleanField(default=False)
    priority = models.CharField(max_length=11, choices=PRIORITY_CHOICES, default="C")
    task_type = models.ForeignKey(TaskType, on_delete=models.CASCADE)
    assignees = models.ManyToManyField(Worker)

    def __str__(self):
        return self.name
