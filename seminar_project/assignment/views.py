from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Assignment, Submission
from .serializers import AssignmentSerializer, SubmissionSerializer
from django.shortcuts import get_object_or_404
from django.utils import timezone

@api_view(['POST'])
def assignment_create(request):
    if request.method == 'POST':
        serializer = AssignmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def all_assignments_list(request):
    assignments = Assignment.objects.all()
    serializer = AssignmentSerializer(assignments, many=True)
    return Response(serializer.data)

@api_view(['GET', 'PUT', 'DELETE'])
def assignment_rud(request, pk):
    assignment = get_object_or_404(Assignment, pk=pk)
    if request.method == 'GET':
        serializer = AssignmentSerializer(assignment)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = AssignmentSerializer(assignment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        assignment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
def submission_create(request, pk):
    assignment = get_object_or_404(Assignment, pk=pk)
    if request.method == 'POST':
        serializer = SubmissionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(assignment=assignment)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def submissions_by_assignment_list(request, pk):
    submissions = Submission.objects.filter(assignment_id=pk)
    serializer = SubmissionSerializer(submissions, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def assignments_by_part_list(request, part_name):
    assignments = Assignment.objects.filter(part__name=part_name)
    serializer = AssignmentSerializer(assignments, many=True)
    return Response(serializer.data)