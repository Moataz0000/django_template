from apps.users.models.user import MobileUser
from django.db import models
from ..other.choices import StudentClassChoices
from django.core.exceptions import ValidationError



class Student(MobileUser):
    class_number = models.IntegerField(choices=StudentClassChoices.choices, default=StudentClassChoices.CLASS_A)


    def validate_full_name(self):
        """Ensure full_name is not empty with the student."""
        if not self.full_name:
            raise ValidationError({'full_name': 'Full Name must be set!'})

    def clean(self):
        self.validate_full_name()
