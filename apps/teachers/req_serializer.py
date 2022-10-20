from rest_framework import serializers
from apps.students.models import Assignment


class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = "__all__"

    def validate(self, attrs):
        if "content" in attrs and attrs["content"] == "PASSED":
            raise serializers.ValidationError("Teacher cannot change the student who submitted the assignment")

        else:
            raise serializers.ValidationError("Teacher cannot grade for other teacher" "s assignment")

        if self.partial:
            return attrs

        return super().validate(attrs)
