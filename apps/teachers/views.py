from rest_framework import generics, status
from rest_framework.response import Response

from apps.teachers.models import Teacher

from apps.students.models import Assignment, Student
from apps.students.serializers import StudentAssignmentSerializer
from apps.teachers.serializers import TeacherAssignmentSerializer


class AssignmentsView(generics.ListCreateAPIView):
    student_serializer_class = StudentAssignmentSerializer
    teacher_serializer_class = TeacherAssignmentSerializer

    def get(self, request, *args, **kwargs):
        print(request)
        assignments = Assignment.objects.filter(teacher__user=request.user)

        return Response(
            data=self.student_serializer_class(assignments, many=True).data,
            status=status.HTTP_200_OK
        )

    def patch(self, request, *args, **kwargs):
        teacher = Teacher.objects.get(user=request.user)
        request.data['teacher'] = teacher.id

        try:
            assignment = Assignment.objects.get(pk=request.data['id'], teacher__user=request.user)
        except Assignment.DoesNotExist:
            return Response(
                data={'error': 'Assignment does not exist/permission denied'},
                status=status.HTTP_400_BAD_REQUEST
            )

        request.data['state'] = assignment.state

        serializer = self.teacher_serializer_class(assignment, data=request.data, partial=True)

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
