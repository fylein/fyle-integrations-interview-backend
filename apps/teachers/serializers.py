from xml.etree.ElementTree import SubElement
from attr import attr
from pytest import Instance
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

        if 'content' in attrs:
            raise serializers.ValidationError('Teacher cannot change the content of the assignment')

        if 'student' in attrs:
            raise serializers.ValidationError('Teacher cannot change the student who submitted the assignment')
        
        if self.instance.teacher.user != self._context['principal']:
            raise serializers.ValidationError('Teacher cannot grade for other teacher''s assignment')

        if self.instance.state == 'DRAFT':
            raise serializers.ValidationError('SUBMITTED assignments can only be graded')
        if self.instance.grade is not None:
            raise serializers.ValidationError('GRADED assignments cannot be graded again')


        if self.partial:
            return attrs

        return super().validate(attrs)

    def update(self,instance,validated_data):

        instance.state=validated_data.get('state',instance.state)
        instance.grade=validated_data.get('grade',instance.grade)
        return instance

