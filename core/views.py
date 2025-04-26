from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegistrationForm, ClientForm

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

