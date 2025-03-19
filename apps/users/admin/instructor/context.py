from typing import Optional
from django.http import HttpRequest
from apps.users.models.instructor import Instructor


class InstructorContextLogic:
    def __init__(self, request: HttpRequest, instructor: Optional[Instructor] = None):
        self.request = request
        self.instructor = instructor

    @property
    def is_superuser(self) -> bool:
        return self.request.user.is_superuser

    @property
    def is_staff(self) -> bool:
        return self.request.user.is_staff

    @property
    def is_creating(self) -> bool:
        return self.instructor is None
