from rest_framework import serializers
from .models import Part, Assignment, Submission

class PartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Part
        fields = # 구현

class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = # 구현

class SubmissionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Submission
        fields = # 구현