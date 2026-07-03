from django.shortcuts import render

def attendance_list(request):
    return render(request, "attendance/attendance_list.html")
