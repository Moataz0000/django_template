from unfold.decorators import display
from apps.users.models.student import Student

class StudentDisplayMixin:
    @display(description="student", header=True)
    def display_header(self, student: Student):
        """Display header with image if available."""
        return [
            student.pk,
            "",
            "O",
            {"path": student.image.url if hasattr(student, 'image') and student.image else None},
        ]
