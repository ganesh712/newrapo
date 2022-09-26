from rest_framework import serializers
from .models import Student
#from .serializers import StudentSerializer
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id','name','roll','city']


