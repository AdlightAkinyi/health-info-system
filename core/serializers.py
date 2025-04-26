from rest_framework import serializers
from .models import Program, Client, Enrollment
from django.contrib.auth.models import User

class ProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = Program
        fields = ['id', 'name', 'description']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class ClientSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Client
        fields = ['id', 'user', 'full_name', 'date_of_birth', 'gender', 'age']

class EnrollmentSerializer(serializers.ModelSerializer):
    client = ClientSerializer()
    program = ProgramSerializer()

    class Meta:
        model = Enrollment
        fields = ['id', 'client', 'program', 'date_enrolled']
