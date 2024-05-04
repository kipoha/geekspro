from django.db import models

# Create your models here.

class Task(models.Model):
    title = models.TimeField(max_length=100)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    created = models.DateTimeField()