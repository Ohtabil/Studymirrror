# student_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('submit_assignment/<int:assignment_id>/', views.submit_assignment, name='submit-assignment'),
]