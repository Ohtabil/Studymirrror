# assignments/models.py
from django.db import models
from django.contrib.auth.models import User

class Assignment(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    due_date = models.DateTimeField()

    # Add any additional fields or methods as needed

    def __str__(self):
        return self.title

class Submission(models.Model):
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    submission_date = models.DateTimeField(auto_now_add=True)
    response = models.TextField()

    # Add any additional fields or methods as needed

    def __str__(self):
        return f"{self.student.username} - {self.assignment.title}"

