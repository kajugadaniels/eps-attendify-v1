from django import forms
from home.models import *

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'national_id', 'email', 'department', 'position', 'date_of_hire', 'tag_id', 'phone_number', 'address', 'day_salary', 'week_ending', 'budget_ref', 'supervision', 'field', 'type', 'nid', 'rssb_number', 'rate', 'gross']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'required': 'true'}),
            'national_id': forms.NumberInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'department': forms.TextInput(attrs={'class': 'form-control'}),
            'position': forms.Select(attrs={'class': 'form-control'}),
            'date_of_hire': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'tag_id': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.NumberInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'day_salary': forms.NumberInput(attrs={'class': 'form-control'}),
            'week_ending': forms.TextInput(attrs={'class': 'form-control', 'required': 'true'}),
            'budget_ref': forms.TextInput(attrs={'class': 'form-control', 'required': 'true'}),
            'supervision': forms.TextInput(attrs={'class': 'form-control', 'required': 'true'}),
            'field': forms.TextInput(attrs={'class': 'form-control', 'required': 'true'}),
            'type': forms.TextInput(attrs={'class': 'form-control', 'required': 'true'}),
            'nid': forms.TextInput(attrs={'class': 'form-control', 'required': 'true'}),
            'rssb_number': forms.TextInput(attrs={'class': 'form-control', 'required': 'true'}),
            'rate': forms.TextInput(attrs={'class': 'form-control', 'required': 'true'}),
            'gross': forms.TextInput(attrs={'class': 'form-control', 'required': 'true'}),
        }
