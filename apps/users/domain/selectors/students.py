from apps.users.models.student import Student
from django.db import models



class StudentSelector:
    
    @staticmethod
    def student_list(filters=None, order_by=None) -> models.QuerySet:
        queryset = Student.objects.all()
        
        if filters:
            queryset = queryset.filter(**filters)
        
        if order_by:
            queryset = queryset.order_by(*order_by)
        
        return queryset
