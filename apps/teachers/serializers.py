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
        
        if 'content' in attrs and attrs['content']:
            raise serializers.ValidationError('Teacher cannot change the content of the assignment')

        if 'state' in attrs:
            if attrs['state'] == 'DRAFT':
                raise serializers.ValidationError('SUBMITTED assignments can only be graded')
            if attrs['state'] == 'GRADED':
                raise serializers.ValidationError('GRADED assignments cannot be graded again')

        if self.partial:
            return attrs

        return super().validate(attrs)
