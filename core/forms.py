from django import forms
from .models import Program, Client
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match")

        return cleaned_data
# User Registration Form
class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

# Client Form
class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['first_name', 'last_name', 'date_of_birth', 'gender', 'phone_number', 'address']

    def save(self, user=None, commit=True):
        client = super().save(commit=False)
        if user:
            client.user = user
        if commit:
            client.save()
        return client

# Program Form (for creating programs)
class ProgramForm(forms.ModelForm):
    class Meta:
        model = Program
        fields = ['name', 'description']  # Add any additional fields that belong to the Program model

       
class EnrollmentForm(forms.Form):
    client = forms.ModelChoiceField(queryset=Client.objects.all())
    programs = forms.ModelMultipleChoiceField(queryset=Program.objects.all())