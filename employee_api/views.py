from django.shortcuts import render

# Create your views here.

def employee_list(request):
    return render(request, "employee_api/employee_list.html")
