from django.contrib import admin
from .list_view import StudentListView
from .change_view import StudentChangeView
from .permissions import StudentPermissions
from .display import StudentDisplayMixin
from apps.users.models.student import Student
from django_model_suite.admin import BaseModelAdmin

@admin.register(Student)
class StudentAdmin(
    StudentDisplayMixin,
    StudentListView,
    StudentChangeView,
    StudentPermissions,
    BaseModelAdmin,
):
    pass
