from django.db import models
from django.contrib.auth.models import User

class Client(models.Model):
    f_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20, unique=True)  
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)  
    
    def str(self):
        return self.f_name