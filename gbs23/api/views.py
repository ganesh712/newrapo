from django.shortcuts import render
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerilaizer
from rest_framework import status
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.

@api_view(['GET','POST','PUT','PATCH','DELETE'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def student_api(request, pk=None):
    if request.method == 'GET':
        id = pk
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerilaizer(stu)
            return Response(serializer.data)
        stu = Student.objects.all()
        serializer = StudentSerilaizer(stu, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = StudentSerilaizer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)

    if request.method == 'PUT':
        id = pk
        stu = Student.objects.get(pk=id)
        serializer = StudentSerilaizer(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Complete Data Updated'})
        return Response(serializer.errors)

    if request.method == 'PATCH':
        id = pk
        stu = Student.objects.get(pk=id)
        serializer = StudentSerilaizer(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Partical Data Updated'})
        return Response(serializer.errors)

    if request.method == 'DELETE':
        id = pk
        stu = Student.objects.get(pk=id)
        stu.delete()
        return Response({'msg':'Data Deleted'})