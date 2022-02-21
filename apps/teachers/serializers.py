from rest_framework import serializers
from .models import Teacher
from apps.students.models import Assignment

class TeacherAssignmentSerializer(serializers.ModelSerializer):
    """
    Teacher Assignment serializer
    """
    class Meta:
        model = Assignment
        fields = '__all__'
    
    def validate(self, attrs):
        attrs = dict(attrs)
        # print(attrs)
        # print(self.context['request'].data)
        # if attrs['grade'] == 'SUBMITTED' and 'grade' in attrs:
        #     raise serializers.ValidationError('SUBMITTED assignments can only be graded')
        
        if attrs['state'] == 'DRAFT' and 'content' not in self.context['request'].data:
            raise serializers.ValidationError('SUBMITTED assignments can only be graded')

        if attrs['state'] == 'GRADED':
            raise serializers.ValidationError('GRADED assignments cannot be graded again')

        if attrs['state'] == 'DRAFT' and 'content' in self.context['request'].data:
            raise serializers.ValidationError('Teacher cannot change the content of the assignment')

        if 'grade' in self.context['request'].data:
            if len(self.context['request'].data['grade']) > 1:
                raise serializers.ValidationError({'grade':['is not a valid choice.']})
                
        if self.partial:
            return attrs

        attrs['state']='GRADED'
        return super().validate(attrs)
