from attr import attr
from rest_framework import serializers
from apps.students.models import Assignment


class TeacherAssignmentSerializer(serializers.ModelSerializer):
    """
    Teacher Assignment serializer
    """
    class Meta:
        model = Assignment
        fields = '__all__'

    def validate(self, attrs):
        if 'grade' in attrs and attrs['grade'] and not attrs['teacher']:
            raise serializers.ValidationError('Student cannot set grade for assignment')

        if 'state' in attrs:
            if attrs['state'] == 'DRAFT':
                raise serializers.ValidationError('Assignment is not submitted by student')

        if self.partial:
            return attrs

        return super().validate(attrs)
