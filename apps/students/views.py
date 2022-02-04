from rest_framework import generics, status
from rest_framework.response import Response

from apps.teachers.models import Teacher

from .models import Assignment, Student
from .serializers import StudentAssignmentSerializer


class AssignmentsView(generics.ListCreateAPIView):
    serializer_class = StudentAssignmentSerializer

    def get(self, request, *args, **kwargs):
        assignments = Assignment.objects.filter(student__user=request.user)

        return Response(
            data=self.serializer_class(assignments, many=True).data,
            status=status.HTTP_200_OK
        )

    def post(self, request, *args, **kwargs):
        student = Student.objects.get(user=request.user)
        request.data['student'] = student.id

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(
                data=serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            data=serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def patch(self, request, *args, **kwargs):
        student = Student.objects.get(user=request.user)
        request.data['student'] = student.id

        if 'teacher_id' in request.data:
            teacher = Teacher.objects.get(pk=request.data['teacher_id'])
            request.data['teacher'] = teacher.id

        try:
            assignment = Assignment.objects.get(pk=request.data['id'], student__user=request.user)
        except Assignment.DoesNotExist:
            return Response(
                data={'error': 'Assignment does not exist/permission denied'},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = self.serializer_class(assignment, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(
                data=serializer.data,
                status=status.HTTP_200_OK
            )

        return Response(
            data=serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
