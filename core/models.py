from django.db import models
from django.contrib.auth.models import User

class Program(models.Model):
    """
    Represents a Health Program (e.g., TB, Malaria, HIV).
    """
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = 'Health Program'
        verbose_name_plural = 'Health Programs'

class Client(models.Model):
    """
    Represents a Client/Patient registered in the system.
    """
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=200)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)

    def __str__(self):
        return self.full_name

    @property
    def age(self):
        from datetime import date
        today = date.today()
        return today.year - self.date_of_birth.year - (
            (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day)
        )

    class Meta:
        ordering = ['full_name']
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'

class Enrollment(models.Model):
    """
    Represents the enrollment of a Client into a Health Program.
    """
    client = models.ForeignKey(Client, related_name="enrollments", on_delete=models.CASCADE)
    program = models.ForeignKey(Program, related_name="enrollments", on_delete=models.CASCADE)
    date_enrolled = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.client.full_name} enrolled in {self.program.name}"

    class Meta:
        unique_together = ('client', 'program')
        ordering = ['-date_enrolled']
        verbose_name = 'Enrollment'
        verbose_name_plural = 'Enrollments'
