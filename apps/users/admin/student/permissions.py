from typing import Optional, Dict
from django.http import HttpRequest
from ...fields.student import StudentFields
from django_model_suite.admin import FieldPermissions
from apps.users.models.student import Student
from .context import StudentContextLogic


class StudentPermissions:
    def has_add_permission(self, request: HttpRequest) -> bool:
        return True

    def has_change_permission(self, request: HttpRequest, student: Optional[Student] = None) -> bool:
        return True

    def has_delete_permission(self, request: HttpRequest, student: Optional[Student] = None) -> bool:
        return True

    def get_field_rules(self, request: HttpRequest, student: Optional[Student] = None) -> Dict:
        context = StudentContextLogic(request, student)

        return {
            StudentFields.PASSWORD: FieldPermissions(
                visible=(
                    context.is_superuser
                ),
                editable=(

                ),
            ),
            StudentFields.LAST_LOGIN: FieldPermissions(
                visible=(
                    context.is_superuser
                ),
                editable=(
                ),
            ),
            StudentFields.IS_SUPERUSER: FieldPermissions(
                visible=(
                    context.is_superuser
                ),
                editable=(
                ),
            ),
            StudentFields.POLYMORPHIC_CTYPE: FieldPermissions(
                visible=(
                    context.is_superuser
                ),
                editable=(
                ),
            ),
            StudentFields.USERNAME: FieldPermissions(
                visible=(
                    context.is_superuser
                ),
                editable=(
                    context.is_superuser
                ),
            ),
            StudentFields.IS_ACTIVE: FieldPermissions(
                visible=(
                    context.is_superuser
                ),
                editable=(
                ),
            ),
            StudentFields.IS_STAFF: FieldPermissions(
                visible=(
                    context.is_superuser
                ),
                editable=(
                ),
            ),
            StudentFields.DATE_JOINED: FieldPermissions(
                visible=(
                    context.is_superuser
                ),
                editable=(
                ),
            ),
            StudentFields.GROUPS: FieldPermissions(
                visible=(
                    context.is_superuser
                ),
                editable=(
                ),
            ),
            StudentFields.USER_PERMISSIONS: FieldPermissions(
                visible=(
                    context.is_superuser
                ),
                editable=(
                ),
            ),
            StudentFields.PHONE_NUMBER: FieldPermissions(
                visible=(
                    context.is_superuser
                ),
                editable=(
                    context.is_superuser
                ),
            ),
            StudentFields.IMAGE: FieldPermissions(
                visible=(
                    context.is_superuser
                ),
                editable=(
                    context.is_superuser
                ),
            ),
            StudentFields.FULL_NAME: FieldPermissions(
                visible=(
                    context.is_superuser
                ),
                editable=(
                    context.is_superuser
                ),
            ),
            StudentFields.CLASS_NUMBER: FieldPermissions(
                visible=(
                    context.is_superuser
                ),
                editable=(
                    context.is_superuser
                ),
            )
        }
