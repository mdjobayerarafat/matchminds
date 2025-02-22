from django.urls import path
from .views import (
    JobSeekerRegistrationView,
    EmployerRegistrationView,
    LoginView,
    JobSeekerDashboardView,
    EmployerDashboardView
)

urlpatterns = [
    path('register/jobseeker/', JobSeekerRegistrationView.as_view(), name='jobseeker_register'),
    path('register/employer/', EmployerRegistrationView.as_view(), name='employer_register'),
    path('login/', LoginView.as_view(), name='login'),
    path('dashboard/jobseeker/', JobSeekerDashboardView.as_view(), name='jobseeker_dashboard'),
    path('dashboard/employer/', EmployerDashboardView.as_view(), name='employer_dashboard'),
]