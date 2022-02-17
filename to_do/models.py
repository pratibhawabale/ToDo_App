
from django.db import models
from datetime import datetime 
from django.contrib.auth.models import User

# Create your models here.
STATUS = (
    ("True", "Completed"),
    ("False", "To be Completed"),
)
class ToDo(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    #owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    deadline = models.DateField(default=datetime.now, blank=True, null=True)
    completed = models.CharField(max_length=20, choices=STATUS, default=False, null=True, blank=True)
    

    def __str__(self) -> str:
        return self.title


