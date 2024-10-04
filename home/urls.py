from django.urls import path
from django.conf import settings
from home.views import *
from django.conf.urls.static import static

app_name = 'base'

urlpatterns = [
    path('dashboard/', dashboard, name="dashboard"),

    path('employees/', getEmployees, name="getEmployees"),
    path('employee/add/', addEmployees, name="addEmployees"),
    path('employee/<int:id>/edit/', editEmployees, name="editEmployees"),
    path('employee/<int:id>/', viewEmployees, name="viewEmployees"),
    path('employee/<int:id>/', deleteEmployees, name="deleteEmployees"),
    path('attendance/record/', recordAttendance, name='recordAttendance'),
    path('attendance/', getAttendance, name='getAttendance'),
]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)