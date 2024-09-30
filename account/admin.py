from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _
from account.models import *

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone_number', 'role', 'added_by', 'is_active', 'is_staff')
    search_fields = ('name', 'email', 'phone_number')
    prepopulated_fields = {'slug': ('name',)}