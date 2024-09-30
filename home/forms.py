from django import forms
from home.models import *

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'national_id', 'email', 'department', 'position', 'date_of_hire', 'tag_id', 'phone_number', 'address']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'required': 'true'}),
            'national_id': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'department': forms.TextInput(attrs={'class': 'form-control'}),
            'position': forms.Select(attrs={'class': 'form-control'}),
            'date_of_hire': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'tag_id': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control'}),
        }
