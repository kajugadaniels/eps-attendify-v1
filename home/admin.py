from home.models import *
from django.contrib import admin

@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['name', 'national_id', 'email', 'department', 'position', 'date_of_hire', 'tag_id', 'phone_number', 'address', 'day_salary']
    search_fields = ['name', 'national_id', 'email']
    list_filter = ['department', 'position', 'date_of_hire']

@admin.register(EmployeeAttendance)
class EmployeeAttendanceAdmin(admin.ModelAdmin):
    list_display = ('employee', 'attended', 'created_at')
    list_filter = ('attended', 'created_at', 'employee')
    search_fields = ('employee__name', 'employee__national_id', 'employee__tag_id')