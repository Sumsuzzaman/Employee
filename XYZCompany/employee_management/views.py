from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from .forms import EmployeeForm, EmployeeUpdateForm
from .models import Employee

# Utility function to check if the user is a superuser
def is_superuser(user):
    return user.is_superuser

# View to display all employees on the homepage
def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employee_management/employee_list.html', {'employees': employees})

# View to add a new employee (restricted to superusers)
@user_passes_test(is_superuser)
def add_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm()
    return render(request, 'employee_management/add_employee.html', {'form': form})

# View to update an employee's details (restricted to superusers)
@user_passes_test(is_superuser)
def update_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        form = EmployeeUpdateForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeUpdateForm(instance=employee)
    return render(request, 'employee_management/update_employee.html', {'form': form})

# View to delete an employee (restricted to superusers)
@user_passes_test(is_superuser)
def delete_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        employee.delete()
        return redirect('employee_list')
    return render(request, 'employee_management/delete_employee.html', {'employee': employee})
