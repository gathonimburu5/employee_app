from .models import Attendance, Shift, ShiftAssignment, AttendanceLog
from django.db import transaction

class AttendanceService:
    @staticmethod
    def getAllAttendanceList():
        return Attendance.objects.all().order_by("-id")

    @staticmethod
    def getAllShiftList():
        return Shift.objects.all().order_by("-id")

    @staticmethod
    @transaction.Atomic
    def createShiftRecord(name, startTime, endTime, breakStart, breakEnd, gracePeriod, lateAfter, earlyCheckout, workingHrs, isNightShift, createdBy=None):
        try:
            shift = Shift(
                shift_name=name,
                start_time=startTime,
                end_time=endTime,
                break_start=breakStart,
                break_end=breakEnd,
                grace_period=gracePeriod,
                late_after=lateAfter,
                early_checkout=earlyCheckout,
                working_hours=workingHrs,
                is_night_shift=isNightShift,
                created_by=createdBy
            )
            shift.save()
            return shift
        except Exception as e:
            raise ValueError(f"Error creating shift: {str(e)}")
