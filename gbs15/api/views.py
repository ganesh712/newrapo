from .models import Student
from .serializers import StudentSerializer
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView,UpdateAPIView, ListCreateAPIView, RetrieveUpdateAPIView


class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class Studentcreate(CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentRetrieve(RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class Studentupdate(UpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentDestroy(UpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentListCreate(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentListRetrieveUpdate(RetrieveUpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer