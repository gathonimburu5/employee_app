from django.db import models
from django.contrib.auth.models import User

status_choices = [('active', 'Active'), ('inactive', 'Inactive'), ('terminated', 'Terminated'), ('on_leave', 'On Leave'), ('suspended', 'Suspended'), ('retired', 'Retired')]
gender_choices = [('male', 'Male'), ('female', 'Female')]

class Department(models.Model):
    department_name = models.CharField(max_length=100, unique=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="departments_created")

    class Meta:
        ordering = ['department_name']

    def __str__(self):
        return self.department_name

class Position(models.Model):
    position_name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="positions_created")

    class Meta:
        ordering = ['position_name']

    def __str__(self):
        return self.position_name

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True)
    employee_id = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email_address = models.CharField(unique=True)
    phone_number = models.CharField(max_length=15)
    postal_address = models.CharField(max_length=255)
    physical_address = models.CharField(max_length=255)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    position = models.ForeignKey(Position, on_delete=models.SET_NULL, null=True)
    date_of_birth = models.DateField()
    date_of_hire = models.DateField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    kra_pin = models.CharField(max_length=20, blank=True, null=True)
    nssf_number = models.CharField(max_length=20, blank=True, null=True)
    shif_number = models.CharField(max_length=20, blank=True, null=True)
    bank_account_number = models.CharField(max_length=20, blank=True, null=True)
    bank_name = models.CharField(max_length=100, blank=True, null=True)
    bank_branch = models.CharField(max_length=100, blank=True, null=True)
    bank_swift_code = models.CharField(max_length=20, blank=True, null=True)
    status = models.CharField(max_length=20, choices=status_choices, default='active')
    gender = models.CharField(max_length=10, choices=gender_choices, blank=True, null=True)
    employee_photo = models.ImageField(upload_to='employees/', blank=True, null=True)
    emergency_contact_name = models.CharField(max_length=100, blank=True, null=True)
    emergency_contact_relationship = models.CharField(max_length=50, blank=True, null=True)
    emergency_contact_phone = models.CharField(max_length=15, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="employees_created")
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="employees_updated")

    class Meta:
        ordering = ['employee_id']

    @property
    def full_name(self):
        return " ".join(filter(None, [self.first_name, self.middle_name, self.last_name]))

    @property
    def address(self):
        return " ".join(filter(None, [self.postal_address, self.physical_address]))

    def __str__(self):
        return f"{self.employee_id} {self.first_name} {self.last_name}"
