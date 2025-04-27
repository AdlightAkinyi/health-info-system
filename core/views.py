from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.http import Http404
from .forms import UserRegistrationForm, ClientForm, ProgramForm  # Add ProgramForm
from .models import Program, Client, Enrollment
from rest_framework import generics
from .serializers import ProgramSerializer, ClientSerializer, EnrollmentSerializer
from .forms import EnrollmentForm 
from .models import Client  # Assuming you have a Client model
from .forms import SignUpForm
from django.shortcuts import render

def login_view(request):
    return render(request, 'login.html')

def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])  # Hash the password
            user.save()
            login(request, user)  # Log the user in immediately after sign-up
            return redirect('home')  # Redirect to home page or any other page
    else:
        form = SignUpForm()
    
    return render(request, 'core/signup.html', {'form': form})

def client_list(request):
    clients = Client.objects.all()  # Fetch all clients
    return render(request, 'client_list.html', {'clients': clients})

def enroll_client(request):
    if request.method == "POST":
        form = EnrollmentForm(request.POST)
        if form.is_valid():
            # Enroll the client in the selected program(s)
            client = form.cleaned_data['client']
            programs = form.cleaned_data['programs']
            for program in programs:
                client.programs.add(program)
            return redirect('client_list')  # Redirect to client list or another page
    else:
        form = EnrollmentForm()

    return render(request, 'enroll_client.html', {'form': form})

# User Registration View
def signup(request):
    if request.method == "POST":
        user_form = UserRegistrationForm(request.POST)
        client_form = ClientForm(request.POST)
        if user_form.is_valid() and client_form.is_valid():
            user = user_form.save()
            client = client_form.save(user=user)
            login(request, user)
            return redirect('home')
    else:
        user_form = UserRegistrationForm()
        client_form = ClientForm()
    return render(request, 'signup.html', {'user_form': user_form, 'client_form': client_form})

# Login View
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

# Home View (List Programs & Clients)
def home(request):
    programs = Program.objects.all()
    query = request.GET.get('q', '')
    clients = Client.objects.filter(user__username__icontains=query)  # Simple search by username
    return render(request, 'home.html', {'programs': programs, 'clients': clients})

# Client Profile View (View Client Details and Enrollments)
def client_profile(request, client_id):
    try:
        client = Client.objects.get(id=client_id)
    except Client.DoesNotExist:
        raise Http404("Client not found")
    
    enrollments = client.enrollments.all()
    return render(request, 'client_profile.html', {'client': client, 'enrollments': enrollments})

# Enroll Client in Programs (New Enrollment)
def enroll_client(request, client_id):
    try:
        client = Client.objects.get(id=client_id)
    except Client.DoesNotExist:
        raise Http404("Client not found")
    
    programs = Program.objects.all()
    if request.method == 'POST':
        selected_programs = request.POST.getlist('programs')
        for program_id in selected_programs:
            try:
                program = Program.objects.get(id=program_id)
                Enrollment.objects.create(client=client, program=program)
            except Program.DoesNotExist:
                pass  # You can add logging here if necessary
        return redirect('client_profile', client_id=client.id)
    
    return render(request, 'enroll_client.html', {'client': client, 'programs': programs})

# Create a New Program View
def create_program(request):
    if request.method == 'POST':
        form = ProgramForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to home or program list after successful creation
    else:
        form = ProgramForm()
    
    return render(request, 'create_program.html', {'form': form})
    

# List and Create Programs (API)
class ProgramListCreateView(generics.ListCreateAPIView):
    queryset = Program.objects.all()
    serializer_class = ProgramSerializer

# List and Create Clients (API)
class ClientListCreateView(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

# List and Create Enrollments (API)
class EnrollmentListCreateView(generics.ListCreateAPIView):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer

# Retrieve a Single Client Profile by ID (API)
class ClientDetailView(generics.RetrieveAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

# Client Search API (to search clients by name)
class ClientSearchView(generics.ListAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

    def get_queryset(self):
        query = self.request.GET.get('q', '')
        return Client.objects.filter(user__username__icontains=query)  # Search by client name
