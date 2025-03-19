from apps.users.models.student import Student
from rest_framework_simplejwt.token_blacklist.models import BlacklistedToken
from rest_framework_simplejwt.token_blacklist.models import OutstandingToken
from rest_framework_simplejwt.tokens import RefreshToken
from apps.users.models import User


class StudentService:
    @staticmethod
    def create_student(*, username: str, phone_number: str, full_name: str, class_number: int) -> Student:
        student = Student(
            username=username,
            phone_number=phone_number,
            full_name=full_name,
            class_number=class_number,
        )
        student.full_clean()
        student.save()
        return student
    


class UserServices:
    @staticmethod
    def generate_token_for_user(user: User) -> dict[str, str]:
        refresh_token = RefreshToken.for_user(user)
        return {
            "access": str(refresh_token.access_token),
            "refresh": str(refresh_token),
        }

    @staticmethod
    def user_logout(user):

        tokens = OutstandingToken.objects.filter(user_id=user.id)
        if tokens.exists():
            for token in tokens:
                BlacklistedToken.objects.get_or_create(token=token)

