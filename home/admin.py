from home.models import *
from django.contrib import admin

@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['name', 'national_id', 'email', 'department', 'position', 'date_of_hire', 'tag_id', 'phone_number', 'address']
    search_fields = ['name', 'national_id', 'email']
    list_filter = ['department', 'position', 'date_of_hire']