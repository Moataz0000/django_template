from django.contrib import admin
from .list_view import InstructorListView
from .change_view import InstructorChangeView
from .permissions import InstructorPermissions
from .display import InstructorDisplayMixin
from apps.users.models.instructor import Instructor
from django_model_suite.admin import BaseModelAdmin

@admin.register(Instructor)
class InstructorAdmin(
    InstructorDisplayMixin,
    InstructorListView,
    InstructorChangeView,
    InstructorPermissions,
    BaseModelAdmin,
):
    pass
