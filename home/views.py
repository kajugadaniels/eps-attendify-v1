from home.forms import *
from home.models import *
from django.contrib import messages
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
    employees = Employee.objects.all().order_by('-date_of_hire')

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
            return redirect('viewEmployees', id=employee.id)
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