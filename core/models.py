from django.db import models
from django.contrib.auth.models import User

class Program(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=200)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10)

    def __str__(self):
        return self.full_name

class Enrollment(models.Model):
    client = models.ForeignKey(Client, related_name="enrollments", on_delete=models.CASCADE)
    program = models.ForeignKey(Program, related_name="enrollments", on_delete=models.CASCADE)
    date_enrolled = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.client.full_name} - {self.program.name}"
