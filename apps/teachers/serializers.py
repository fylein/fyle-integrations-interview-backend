from rest_framework import serializers
from apps.students.models import Assignment


class TeacherAssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = '__all__'

    def validate(self, attrs):
        if 'content' in attrs and attrs['content']:
            raise serializers.ValidationError('Teacher cannot change the content of the assignment')
        
        if 'passed_id' in attrs and attrs['passed_id']:
            raise serializers.ValidationError('Teacher cannot change the student who submitted the assignment')
        
        if 'actual_teacher' in attrs and attrs['actual_teacher'] != attrs['teacher']:
            raise serializers.ValidationError('Teacher cannot grade for other teacher''s assignment')
        
        if 'grade' in attrs and attrs['grade'] not in ["A", "B", "C", "D"]:
            raise serializers.ValidationError(
                f"{attrs['grade']} is not a valid choice."
            )
        if 'state' in attrs:
            if attrs['state'] == 'DRAFT':
                raise serializers.ValidationError('SUBMITTED assignments can only be graded')
            if attrs['state'] == 'GRADED':
                raise serializers.ValidationError('GRADED assignments cannot be graded again')
            
        
        if attrs['state'] == 'SUBMITTED':
            attrs['state'] = "GRADED"
 
        if self.partial:
            return attrs

        return super().validate(attrs)
