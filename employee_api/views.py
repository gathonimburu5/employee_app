from django.shortcuts import render, redirect
from django.contrib import messages
from .service import EmployeeService


def employee_list(request):
    employees = EmployeeService.getAllEmployees()
    return render(request, "employee_api/employee_list.html", {"employees": employees})

def department_list(request):
    if request.method == "POST":
        name = request.POST.get("department_name")
        location = request.POST.get("location")
        desciption = request.POST.get("description")
        created_by = request.user if request.user.is_authenticated else None

        EmployeeService.createDepartment(name, location, desciption, created_by)
        messages.success(request, "department created successfully.")
        return redirect("department_list")

    departments = EmployeeService.getAllDepartments()
    return render(request, "employee_api/department_list.html", { "departments":departments })

def position_list(request):
    if request.method == "POST":
        name = request.POST.get("position_name")
        description = request.POST.get("description")
        created_by = request.user if request.user.is_authenticated else None

        EmployeeService.createPosition(name, description, created_by)
        messages.success(request, "position created successfully.")
        return redirect("position_list")

    positions = EmployeeService.getAllPositions()
    return render(request, "employee_api/position_list.html", { "positions":positions })


def employee_create(request):
    departments = EmployeeService.getAllDepartments()
    print(departments)
    positions = EmployeeService.getAllPositions()

    if request.method == "POST":
        # Extract form data
        # user = request.user
        employee_id = request.POST.get("employee_id")
        first_name = request.POST.get("first_name")
        middle_name = request.POST.get("middle_name")
        last_name = request.POST.get("last_name")
        email_address = request.POST.get("email_address")
        phone_number = request.POST.get("phone_number")
        postal_address = request.POST.get("postal_address")
        physical_address = request.POST.get("physical_address")
        department_id = request.POST.get("department")
        position_id = request.POST.get("position")
        date_of_birth = request.POST.get("date_of_birth")
        date_of_hire = request.POST.get("date_of_hire")
        salary = request.POST.get("salary")
        kra_pin = request.POST.get("kra_pin") or None
        nssf_number = request.POST.get("nssf_number") or None
        shif_number = request.POST.get("shif_number") or None
        bank_account_number = request.POST.get("bank_account_number") or None
        bank_name = request.POST.get("bank_name") or None
        bank_branch = request.POST.get("bank_branch") or None
        bank_swift_code = request.POST.get("bank_swift_code") or None
        status = request.POST.get("status") or "active"
        gender = request.POST.get("gender")
        employee_photo = request.FILES.get("employee_photo") or None
        emergency_contact_name = request.POST.get("emergency_contact_name") or None
        emergency_contact_relationship = request.POST.get("emergency_contact_relationship") or None
        emergency_contact_phone = request.POST.get("emergency_contact_phone") or None
        created_by = request.user if request.user.is_authenticated else None

        # Create the employee
        try:
            department = departments.get(id=department_id)
            if not department:
                messages.error(request, "department is required!!")
                return redirect("employee_create")

            position = positions.get(id=position_id)
            if not position:
                messages.error(request, "position is required!!")
                return redirect("employee_create")

            employee_data = {
                "user": None,
                "employee_id": employee_id,
                "first_name": first_name,
                "middle_name": middle_name,
                "last_name": last_name,
                "email_address": email_address,
                "phone_number": phone_number,
                "postal_address": postal_address,
                "physical_address": physical_address,
                "department": department,
                "position": position,
                "date_of_birth": date_of_birth,
                "date_of_hire": date_of_hire,
                "salary": salary,
                "kra_pin": kra_pin,
                "nssf_number": nssf_number,
                "shif_number": shif_number,
                "bank_account_number": bank_account_number,
                "bank_name": bank_name,
                "bank_branch": bank_branch,
                "bank_swift_code": bank_swift_code,
                "status": status,
                "gender": gender,
                "employee_photo": employee_photo,
                "emergency_contact_name": emergency_contact_name,
                "emergency_contact_relationship": emergency_contact_relationship,
                "emergency_contact_phone": emergency_contact_phone
            }

            EmployeeService.createEmployee(employee_data, created_by=created_by)
            messages.success(request, "Employee created successfully.")
            return redirect("employee_list")

        except Exception as e:
            messages.error(request, f"Error creating employee: {str(e)}")
            return redirect("employee_create")

    return render(request, "employee_api/employee_create.html", {"departments": departments, "positions": positions})

