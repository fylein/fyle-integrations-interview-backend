from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from django.forms.models import model_to_dict
from .models import Teacher
from apps.students.models import Assignment
from .serializers import TeacherAssignmentSerializer

class TeacherAssignment(generics.RetrieveUpdateAPIView):
    serializer_class = TeacherAssignmentSerializer
    model = Assignment
    pagination_class = None
    request = None

    def get_object(self, *args, **kwargs):
        queryset = self.model.objects.filter(teacher__user=self.request.user)
        return queryset

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, many=True)
        return Response(serializer.data, status=200)

    def partial_update(self, request, *args, **kwargs):
        try:
            instance = self.model.objects.get(teacher__user=self.request.user, id=request.data['id'])
        except Assignment.DoesNotExist:
            return Response(
                data={'error': 'Assignment does not exist/permission denied'},
                status=status.HTTP_400_BAD_REQUEST
            )
        instance.grade=request.data['grade']
        data = model_to_dict(instance)
        serializer = self.get_serializer(instance, data=data, context={"request":request})

        if serializer.is_valid():
            self.perform_update(serializer)

            return Response(
                data=serializer.data,
                status=200
            )

        return Response(
            data=serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )