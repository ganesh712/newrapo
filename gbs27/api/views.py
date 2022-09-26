from django.shortcuts import render
from .serializers import StudentSerializer
from rest_framework import viewsets
from .models import Student
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    #authentication_classes =  [SessionAuthentication]
    #permission_classes = [IsAuthenticated]
    #permission_classes = [IsAdminUser]
    #permission_classes = [IsAuthenticatedOrReadOnly]
    #permission_classes = [DjangoModelPermissions]


# class StudentModelViewSet(viewsets.ModelViewSet):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#     authentication_classes =  [BasicAuthentication]
#     permission_classes = [AllowAny]
