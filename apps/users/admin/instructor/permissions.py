from typing import Optional, Dict
from django.http import HttpRequest
from ...fields.instructor import InstructorFields
from django_model_suite.admin import FieldPermissions
from apps.users.models.instructor import Instructor
from .context import InstructorContextLogic


class InstructorPermissions:
    def has_add_permission(self, request: HttpRequest) -> bool:
        return False

    def has_change_permission(self, request: HttpRequest, instructor: Optional[Instructor] = None) -> bool:
        return False

    def has_delete_permission(self, request: HttpRequest, instructor: Optional[Instructor] = None) -> bool:
        return False

    def get_field_rules(self, request: HttpRequest, instructor: Optional[Instructor] = None) -> Dict:
        context = InstructorContextLogic(request, instructor)

        return {
            InstructorFields.PASSWORD: FieldPermissions(
                visible=(
                    context.is_superuser
                ),
                editable=(
                ),
            ),
            InstructorFields.LAST_LOGIN: FieldPermissions(
                visible=(
                    context.is_superuser
                ),
                editable=(
                ),
            ),
            InstructorFields.IS_SUPERUSER: FieldPermissions(
                visible=(
                    context.is_superuser
                ),
                editable=(
                ),
            ),
            InstructorFields.POLYMORPHIC_CTYPE: FieldPermissions(
                visible=(
                    context.is_superuser
                ),
                editable=(
                ),
            ),
            InstructorFields.USERNAME: FieldPermissions(
                visible=(
                    context.is_superuser
                ),
                editable=(
                ),
            ),
            InstructorFields.IS_ACTIVE: FieldPermissions(
                visible=(
                    context.is_superuser
                ),
                editable=(
                ),
            ),
            InstructorFields.IS_STAFF: FieldPermissions(
                visible=(
                    context.is_superuser
                ),
                editable=(
                ),
            ),
            InstructorFields.DATE_JOINED: FieldPermissions(
                visible=(
                    context.is_superuser
                ),
                editable=(
                ),
            ),
            InstructorFields.GROUPS: FieldPermissions(
                visible=(
                    context.is_superuser
                ),
                editable=(
                ),
            ),
            InstructorFields.USER_PERMISSIONS: FieldPermissions(
                visible=(
                    context.is_superuser
                ),
                editable=(
                ),
            ),
            InstructorFields.PHONE_NUMBER: FieldPermissions(
                visible=(
                    context.is_superuser
                ),
                editable=(
                ),
            ),
            InstructorFields.IMAGE: FieldPermissions(
                visible=(
                    context.is_superuser
                ),
                editable=(
                ),
            ),
            InstructorFields.FULL_NAME: FieldPermissions(
                visible=(
                    context.is_superuser
                ),
                editable=(
                ),
            ),
            InstructorFields.POSITION: FieldPermissions(
                visible=(
                    context.is_superuser
                ),
                editable=(
                ),
            )
        }
