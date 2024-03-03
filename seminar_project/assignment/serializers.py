from datetime import timezone
from rest_framework import serializers
from .models import Part, Assignment, Submission

class PartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Part
        fields = ['name']  # Part 모델의 모든 필드를 직렬화

class SubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Submission
        fields = ['id', 'content', 'github_link']  # Submission 모델의 모든 필드를 직렬화

class AssignmentSerializer(serializers.ModelSerializer):
    submissions = SubmissionSerializer(many=True, read_only=True)  # SubmissionSerializer를 포함한 필드 추가
    remained_time = serializers.SerializerMethodField()

    class Meta:
        model = Assignment
        fields = ['id', 'title', 'content', 'part', 'github_link', 'created_at', 'expire_at']  # Assignment 모델의 모든 필드를 직렬화
    
    def get_time_difference(self, obj):
        time_difference = obj.expire_at - timezone.now()
        return time_difference 