from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from apps.users.domain.selectors.students import StudentSelector
from apps.users.api.student.serializers import StudentSerializer
from apps.users.domain.services.student import UserServices
from django.core.exceptions import ValidationError


class StudentListView(generics.ListAPIView):
    permission_classes = []
    queryset = StudentSelector.student_list(order_by=['-date_joined'])
    serializer_class = StudentSerializer



class StudentCreateView(generics.GenericAPIView):
    permission_classes = []
    serializer_class = StudentSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            student = serializer.save()  
            tokens = UserServices.generate_token_for_user(student)
            return Response(
                {
                    **tokens,
                    "student": serializer.data,
                },
                status=status.HTTP_201_CREATED,
            )
        except ValidationError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)