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
        # Selecting the list of assignments for the user from DB
        assignments = Assignment.objects.filter(teacher__user=request.user)

        return Response(
            data=self.student_serializer_class(assignments, many=True).data,
            status=status.HTTP_200_OK
        )

    def patch(self, request, *args, **kwargs):
        # Fetch the teacher object for user in request
        teacher = Teacher.objects.get(user=request.user)
        request.data['teacher'] = teacher.id

        try:
            # Fetch the assignment for particular assignment['id']
            assignment = Assignment.objects.get(pk=request.data['id'])
        except Assignment.DoesNotExist:
            # Return error if assignment not found for particular id
            return Response(
                data={'error': 'Assignment does not exist/permission denied'},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Check if student key is there in the request.data
        # Throws error if student key is in the request.data
        if 'student' in request.data:
            student = Student.objects.get(pk=request.data['student'])
            request.data['student'] = student.id
            
            if assignment.student.id != request.data['student']:
                return Response(
                    data={'non_field_errors': ['Teacher cannot change the student who submitted the assignment']},
                    status=status.HTTP_400_BAD_REQUEST
                )

        # Throws error if teacher is trying to access/grade other teacher's assignment
        if assignment.teacher.id != teacher.id:
            return Response(
                data={'non_field_errors': ['Teacher cannot grade for other teachers assignment']},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Storing the current state of assignment
        # Helps in serializer for error handling
        request.data['state'] = assignment.state

        serializer = self.teacher_serializer_class(assignment, data=request.data, partial=True)


        # Returns 200 OK response if serializer is valid with no errors
        if serializer.is_valid():
            serializer.save(state='GRADED')
            return Response(
                data=serializer.data,
                status=status.HTTP_200_OK
            )

        # Returns 400 BAD response if serializer contains no errors
        return Response(
            data=serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
