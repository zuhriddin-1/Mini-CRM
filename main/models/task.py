from django.db import models
from django.contrib.auth.models import User

# Create your models here.

SEMESTER_CHOICES = [
    ("new", "new"),
    ("process", "process"),
    ("done", "done"),

]

class Tasks(models.Model):
    name = models.CharField(max_length=255)
    content = models.TextField()
    status = models.CharField(
        max_length= 255,
        choices=SEMESTER_CHOICES
    )
    doer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="task1")
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="task2")
    client = models.ForeignKey(to="Client", on_delete=models.SET_NULL, related_name="tasks", null=True)
    added_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)