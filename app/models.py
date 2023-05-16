from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=50, default="Generic Task")
    desc = models.TextField(null=True, blank=True)
    PRIORITY_OPTIONS = (
        ("H", "High"),
        ("M", "Medium"),
        ("L", "Low"),
    )
    priority = models.CharField(max_length=1, choices=PRIORITY_OPTIONS, default="M")
    done = models.BooleanField(default=False)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
    def clean(self):
        if not self.title and not self.desc:
            raise ValidationError("Both title and desc fields cannot be empty")
