from django.shortcuts import render
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer
from rest_framework import status
from rest_framework import viewsets

class StudentViewSet(viewsets, viewSet):
    def List(self, request):
        stu = Student.objects.all()
        