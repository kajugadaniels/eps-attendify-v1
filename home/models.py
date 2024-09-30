from django.db import models

class Position(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name

class Employee(models.Model):
    national_id = models.CharField(max_length=20, unique=True, null=True, blank=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    department = models.CharField(max_length=100, null=True, blank=True)
    position = models.ForeignKey(Position, on_delete=models.SET_NULL, null=True, blank=True)
    date_of_hire = models.DateField(null=True, blank=True)
    tag_id = models.CharField(max_length=100, unique=True, null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    address = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} - {self.position.name if self.position else 'No Position'}"