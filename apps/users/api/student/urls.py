from django.urls import path
from .views import (
    StudentListView,
    StudentCreateView,
)



urlpatterns = [
    path('student/list/', StudentListView.as_view(), name='student-list'),
    path('student/create/', StudentCreateView.as_view(), name='student-create')
]
