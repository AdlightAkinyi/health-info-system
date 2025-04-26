from django import forms
from django.contrib.auth.models import User
from .models import Client

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['full_name', 'date_of_birth', 'gender']

    def save(self, user, commit=True):
        client = super().save(commit=False)
        client.user = user
        if commit:
            client.save()
        return client
