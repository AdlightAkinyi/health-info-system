from django.urls import path
from . import views
from .views import (
    ProgramListCreateView,
    ClientListCreateView,
    EnrollmentListCreateView,
    ClientDetailView
)

urlpatterns = [
    # HTML pages
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('clients/<int:client_id>/', views.client_profile, name='client_profile'),
    path('create-program/', views.create_program, name='create_program'),  # New route for creating a program
    path('enroll_client/', views.enroll_client, name='enroll_client'),
    path('clients/', views.client_list, name='client_list'),
    
    
    # API endpoints
    path('api/programs/', ProgramListCreateView.as_view(), name='program-list'),
    path('api/clients/', ClientListCreateView.as_view(), name='client-list'),
    path('api/enrollments/', EnrollmentListCreateView.as_view(), name='enrollment-list'),
    path('api/clients/<int:pk>/', ClientDetailView.as_view(), name='client-detail'),
]
