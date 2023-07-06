# lecturers/views.py
from django.shortcuts import render, redirect
from .models import Assignment

def create_assignment(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        file = request.FILES['file']
        assignment = Assignment.objects.create(title=title, description=description, file=file)
        return redirect('assignments-list')
    return render(request, 'lecturers/create_assignment.html')

