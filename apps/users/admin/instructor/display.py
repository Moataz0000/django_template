from unfold.decorators import display
from apps.users.models.instructor import Instructor

class InstructorDisplayMixin:
    @display(description="instructor", header=True)
    def display_header(self, instructor: Instructor):
        """Display header with image if available."""
        return [
            instructor.pk,
            "",
            "O",
            {"path": instructor.image.url if hasattr(instructor, 'image') and instructor.image else None},
        ]
