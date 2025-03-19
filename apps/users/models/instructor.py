from apps.users.models.user import MobileUser
from django.db import models

class Instructor(MobileUser):
    position = models.CharField(max_length=255, default="", blank=True)


    @property
    def get_username_or_full_name(self) -> str:
        return self.full_name or self.username
    

    @property
    def get_user_info(self) -> str:
        return f"{self.get_username_or_full_name} working as {self.position}"