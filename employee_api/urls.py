from django.urls import path
from . import views

urlpatterns = [
    path("", views.employee_list, name="employee_list"),
    path("create/", views.employee_create, name="employee_create"),
    path("department/", views.department_list, name="department_list"),
    path("position/", views.position_list, name="position_list"),
]