# students/views.py
from django.shortcuts import render, redirect

from lecturers.models import Assignment
from .models import Submission

def submit_assignment(request, assignment_id):
    if request.method == 'POST':
        student = request.user.student  # Assuming student user is authenticated
        assignment = Assignment.objects.get(id=assignment_id)
        file = request.FILES['file']
        submission = Submission.objects.create(student=student, assignment=assignment, file=file)
        return redirect('assignments-list')