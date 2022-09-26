from django.shortcuts import render
from .models import Student
# Create your views here.
from .serializers import StudentSerializer
from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend

class StudentList(ListAPIView):
    queryset = Student.objects.all()
    #queryset = Student.objects.filter(passby='user1')
    serializer_class = StudentSerializer
    filter_backends = [DjangoFilterBackend]
    # def get_queryset(self):
    #     user = self.request.user
    #     return Student.objects.filter(passby=user)
    filterset_fields = ['city']
        
    