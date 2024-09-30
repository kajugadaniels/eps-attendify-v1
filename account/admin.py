from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _
from account.models import *

class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('name', 'phone_number', 'image')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        (_('Role'), {'fields': ('role',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'name', 'phone_number', 'role', 'password1', 'password2'),
        }),
    )
    list_display = ('email', 'name', 'phone_number', 'role', 'is_staff', 'added_by')
    search_fields = ('email', 'name', 'phone_number', 'role')
    ordering = ('email',)

admin.site.register(User, UserAdmin)
