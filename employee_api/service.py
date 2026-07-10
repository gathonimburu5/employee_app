from .models import Employee, Department, Position
from django.db import transaction
from django.utils import timezone

class EmployeeService:
    @staticmethod
    def getAllEmployees():
        return Employee.objects.all().order_by("-id")

    @staticmethod
    def getEmployeeById(employee_id):
        try:
            return Employee.objects.get(id=employee_id)
        except Employee.DoesNotExist:
            raise ValueError(f"Employee with id {employee_id} does not exist.")

    @staticmethod
    def getAllDepartments():
        return Department.objects.all().order_by("-id")

    @staticmethod
    def getAllPositions():
        return Position.objects.all().order_by("-id")

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
    def createEmployee(employee_data, created_by=None):
        employee = Employee.objects.create(**employee_data, created_by=created_by)
        return employee