# lecturers/models.py
from django.db import models

class Assignment(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    file = models.FileField(upload_to='assignments/')
    created_at = models.DateTimeField(auto_now_add=True)

class Quiz(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

