from typing import Optional
from django.http import HttpRequest
from apps.users.models.student import Student


class StudentContextLogic:
    def __init__(self, request: HttpRequest, student: Optional[Student] = None):
        self.request = request
        self.student = student

    @property
    def is_superuser(self) -> bool:
        return self.request.user.is_superuser

    @property
    def is_staff(self) -> bool:
        return self.request.user.is_staff

    @property
    def is_creating(self) -> bool:
        return self.student is None
