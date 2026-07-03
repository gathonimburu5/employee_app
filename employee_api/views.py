from django.shortcuts import render, redirect
from django.contrib import messages
from .service import EmployeeService


def employee_list(request):
    employees = EmployeeService.getAllEmployees()
    return render(request, "employee_api/employee_list.html", {"employees": employees})


def employee_create(request):
    departments = EmployeeService.getAllDepartments()
    positions = EmployeeService.getAllPositions()

    if request.method == "POST":
        # Extract form data
        user = request.user
        employee_id = request.POST.get("employee_id")
        phone_number = request.POST.get("phone_number")
        postal_address = request.POST.get("postal_address")
        physical_address = request.POST.get("physical_address")
        department_id = request.POST.get("department")
        position_id = request.POST.get("position")
        date_of_birth = request.POST.get("date_of_birth")
        date_of_hire = request.POST.get("date_of_hire")
        salary = request.POST.get("salary")
        kra_pin = request.POST.get("kra_pin")
        nssf_number = request.POST.get("nssf_number")
        bank_account_number = request.POST.get("bank_account_number")
        bank_name = request.POST.get("bank_name")
        bank_branch = request.POST.get("bank_branch")
        bank_swift_code = request.POST.get("bank_swift_code")
        status = request.POST.get("status")
        gender = request.POST.get("gender")
        employee_photo = request.FILES.get("employee_photo")
        emergency_contact_name = request.POST.get("emergency_contact_name")
        emergency_contact_relationship = request.POST.get("emergency_contact_relationship")
        emergency_contact_phone = request.POST.get("emergency_contact_phone")
        created_by = request.user if request.user.is_authenticated else None

        # Create the employee
        try:
            department = EmployeeService.getAllDepartments().get(id=department_id)
            position = EmployeeService.getAllPositions().get(id=position_id)

            EmployeeService.createEmployee(
                user=user,
                employee_id=employee_id,
                phone_number=phone_number,
                postal_address=postal_address,
                physical_address=physical_address,
                department=department,
                position=position,
                date_of_birth=date_of_birth,
                date_of_hire=date_of_hire,
                salary=salary,
                kra_pin=kra_pin,
                nssf_number=nssf_number,
                bank_account_number=bank_account_number,
                bank_name=bank_name,
                bank_branch=bank_branch,
                bank_swift_code=bank_swift_code,
                status=status,
                gender=gender,
                employee_photo=employee_photo,
                emergency_contact_name=emergency_contact_name,
                emergency_contact_relationship=emergency_contact_relationship,
                emergency_contact_phone=emergency_contact_phone,
                created_by=created_by
            )
            messages.success(request, "Employee created successfully.")
            return redirect("employee_list")

        except Exception as e:
            messages.error(request, f"Error creating employee: {str(e)}")
            return redirect("employee_create")

    return render(request, "employee_api/employee_create.html", {"departments": departments, "positions": positions})

