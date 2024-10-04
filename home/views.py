from home.forms import *
from home.models import *
from django.utils import timezone
from django.contrib import messages
from django.http import JsonResponse
from datetime import datetime, timedelta
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

@login_required
def dashboard(request):

    context = {
        # 
    }

    return render(request, 'dashboard.html', context)

@login_required
def getEmployees(request):
    employees = Employee.objects.all().order_by('-id')

    context = {
        'employees': employees
    }

    return render(request, 'employees/index.html', context)

@login_required
def addEmployees(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            employee = form.save(commit=False)
            employee.save()
            messages.success(request, 'Employee added successfully.')
            return redirect('base:getEmployees')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
    else:
        form = EmployeeForm()

    context = {
        'form': form
    }

    return render(request, 'employees/create.html', context)

@login_required
def viewEmployees(request, id):
    employee = get_object_or_404(Employee, id=id)

    context = {
        'employee': employee
    }

    return render(request, 'employees/show.html', context)

@login_required
def editEmployees(request, id):
    employee = get_object_or_404(Employee, id=id)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES, instance=employee)
        if form.is_valid():
            employee = form.save(commit=False)
            employee.save()
            messages.success(request, 'Employee updated successfully.')
            return redirect('base:getEmployees', id=employee.id)
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
    else:
        form = EmployeeForm(instance=employee)

    context = {
        'form': form,
        'employee': employee
    }

    return render(request, 'employees/edit.html', context)

@login_required
def deleteEmployees(request, id):
    employee = get_object_or_404(Employee, id=id)
    employee.delete()
    messages.success(request, 'Employee deleted successfully.')
    return redirect('getEmployees')

@csrf_exempt
def recordAttendance(request):
    if request.method == 'POST':
        tag_id = request.POST.get('tag_id')
        if not tag_id:
            return JsonResponse({'status': 'error', 'message': 'No tag_id provided'}, status=400)
        try:
            employee = Employee.objects.get(tag_id=tag_id)
            today = timezone.now().date()
            # Check if attendance for today has already been recorded
            attendance_exists = EmployeeAttendance.objects.filter(employee=employee, created_at__date=today).exists()
            if attendance_exists:
                return JsonResponse({'status': 'error', 'message': 'Attendance already recorded for today'}, status=400)
            # Record attendance
            EmployeeAttendance.objects.create(employee=employee, attended=True)
            return JsonResponse({'status': 'success', 'message': 'Attendance recorded', 'employee': employee.name})
        except Employee.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Employee not found'}, status=404)
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)

@login_required
def getAttendance(request):
    today = timezone.now().date()
    date_range = [today + timedelta(days=i) for i in range(8)]  # Today + next 7 days

    if request.method == 'POST':
        attendance_data = request.POST.getlist('attendance[]')  # List of 'employee_id_date_str'

        for item in attendance_data:
            employee_id, date_str = item.split('_')
            date = datetime.strptime(date_str, '%Y-%m-%d').date()

            if date != today:
                continue  # Only process attendance for today

            employee = Employee.objects.get(id=employee_id)

            # Update or create the attendance record for this employee
            attendance_record, created = EmployeeAttendance.objects.update_or_create(
                employee=employee,
                created_at__date=today,
                defaults={'attended': True, 'created_at': timezone.now()}
            )

        messages.success(request, 'Attendance updated successfully.')
        return redirect('base:getAttendance')

    employees = Employee.objects.all().order_by('name')
    attendance_records = EmployeeAttendance.objects.filter(created_at__date__in=date_range)

    # Build a set of attendance keys for quick lookup in the template
    attendance_set = set()
    for record in attendance_records:
        key = f"{record.employee.id}_{record.created_at.date()}"
        attendance_set.add(key)

    context = {
        'employees': employees,
        'date_range': date_range,
        'attendance_set': attendance_set,
        'today': today,
    }

    return render(request, 'attendance/index.html', context)