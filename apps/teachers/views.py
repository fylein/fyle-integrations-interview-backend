from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework import serializers

from apps.students.models import Assignment
from apps.teachers.serializers import TeacherAssignmentSerializer
from apps.teachers.models import Teacher
# Create your views here.
class AssignmentsView(generics.ListCreateAPIView):
  serializer_class = TeacherAssignmentSerializer
  
  def get(self, request, *args, **kwargs):
  
    assignments = Assignment.objects.filter(teacher__user=request.user)
    
    return Response(
            data=self.serializer_class(assignments, many=True).data,
            status=status.HTTP_200_OK
    )
    
  def patch(self, request, *args, **kwargs):
      teacher = Teacher.objects.get(user=request.user)
        
      if 'student' in request.data:
          request.data._mutable = True
          request.data['passed_id'] = request.data['student']
          request.data.pop('student')
          
          request.data._mutable = False
          
      try:
          assignment = Assignment.objects.get(pk=request.data['id'], teacher__user=request.user)
      except Assignment.DoesNotExist:
          raise serializers.ValidationError('Assignment does not exist/permission denied')
      
    #   request.data._mutable = True
      request.data['teacher'] = teacher.id
      request.data['state'] = assignment.state
      request.data['actual_teacher'] = assignment.teacher.id
      
    #   request.data._mutable = False


      serializer = self.serializer_class(assignment,data=request.data, partial=True)
        


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

    