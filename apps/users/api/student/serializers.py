from apps.users.models.student import Student
from rest_framework import serializers 
from apps.users.domain.services.student import StudentService



class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['username', 'phone_number', 'full_name', 'class_number', 'password']
        extra_kwargs = {
            "class_number": {"required": True}
        }


