from .models import Employee, Department, Position
from django.db import transaction
from django.utils import timezone

class EmployeeService:
    @staticmethod
    def getAllEmployees():
        return Employee.objects.all()

    @staticmethod
    def getEmployeeById(employee_id):
        try:
            return Employee.objects.get(id=employee_id)
        except Employee.DoesNotExist:
            raise ValueError(f"Employee with id {employee_id} does not exist.")

    @staticmethod
    def getAllDepartments():
        return Department.objects.all()

    @staticmethod
    def getAllPositions():
        return Position.objects.all()

    @staticmethod
    @transaction.atomic
    def createDepartment(department_name, location=None, description=None, created_by=None):
        try:
            department = Department(
                department_name=department_name,
                location=location,
                description=description,
                created_by=created_by
            )
            department.save()
            return department

        except Exception as e:
            raise ValueError(f"Error creating department: {str(e)}")

    @staticmethod
    @transaction.atomic
    def createPosition(position_name, description=None, created_by=None):
        try:
            position = Position(
                position_name=position_name,
                description=description,
                created_by=created_by
            )
            position.save()
            return position

        except Exception as e:
            raise ValueError(f"Error creating position: {str(e)}")

    @staticmethod
    @transaction.atomic
    def createEmployee(user, employee_id, phone_number, postal_address, physical_address, department, position, date_of_birth, date_of_hire, salary, kra_pin=None, nssf_number=None, bank_account_number=None,
                       bank_name=None, bank_branch=None, bank_swift_code=None, status='active', gender=None, employee_photo=None, emergency_contact_name=None, emergency_contact_relationship=None, emergency_contact_phone=None,
                       created_by=None):
        try:
            employee = Employee(
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
            employee.save()
            return employee
        except Exception as e:
            raise ValueError(f"Error creating employee: {str(e)}")