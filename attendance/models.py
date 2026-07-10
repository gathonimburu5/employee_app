from django.db import models
from django.contrib.auth.models import User
from employee_api.models import Employee

attendance_status_choices = [
    ('present', 'Present'),
    ('absent', 'Absent'),
    ('late', 'Late'),
    ('on_leave', 'On Leave'),
    ("holiday", "Holiday"),
    ("weekend", "Weekend"),
    ("half_day", "Half Day"),
    ("missed_in", "Missed Check-In"),
    ("missed_out", "Missed Check-Out")
]
attendance_log_choices = [('in', 'IN'), ('out', 'OUT')]

class Shift(models.Model):
    shift_name = models.CharField(max_length=100, unique=True)
    start_time = models.TimeField()
    end_time = models.TimeField()
    break_start = models.TimeField(null=True, blank=True)
    break_end = models.TimeField(null=True, blank=True)
    grace_period = models.IntegerField(default=15)
    late_after = models.IntegerField(default=15)
    early_checkout = models.IntegerField(15)
    working_hours = models.DecimalField(max_digits=5, decimal_places=2)
    is_night_shift = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="shifts_created")
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="shifts_updated")

    class Meta:
        ordering = ['shift_name']

    def __str__(self):
        return self.shift_name

class ShiftAssignment(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    shift = models.ForeignKey(Shift, on_delete=models.CASCADE)
    effective_from = models.DateField()
    effective_to = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.employee.full_name

class Attendance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=20, choices=attendance_status_choices)
    check_in_time = models.TimeField(blank=True, null=True)
    check_out_time = models.TimeField(blank=True, null=True)
    shift = models.ForeignKey(Shift, on_delete=models.PROTECT)
    worked_hours = models.DecimalField(max_digits=5, decimal_places=2)
    overtime_hours = models.DecimalField(max_digits=5, decimal_places=2)
    late_minutes = models.IntegerField(default=0)
    early_leave_minutes = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="attendances_created")
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="attendances_updated")

    class Meta:
        unique_together = ('employee', 'date')
        ordering = ['-date']

    def __str__(self):
        return f"{self.employee.user.get_full_name()} - {self.date} - {self.status}"

class AttendanceLog(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    punch_time = models.DateTimeField()
    device = models.CharField(max_length=100)
    punch_type = models.CharField(max_length=10, choices=attendance_log_choices)

    def __str__(self):
        return self.employee.full_name
