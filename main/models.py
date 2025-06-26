from django.db import models

# Create your models here.
class Client:
    f_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20, unique=True)
    email = models.EmailField(max_length=255)
    address = models.CharField(max_length=255)
    added_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="clients")
