from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import JobSeeker, Employer

class JobSeekerRegistrationForm(UserCreationForm):
    class Meta:
        model = JobSeeker
        fields = ['first_name', 'last_name', 'current_job_title', 'email', 'password1', 'password2']

class EmployerRegistrationForm(UserCreationForm):
    class Meta:
        model = Employer
        fields = ['first_name', 'last_name', 'company_name', 'email', 'password1', 'password2']
