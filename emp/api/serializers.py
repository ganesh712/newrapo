from .models import Employee
from rest_framework import serializers
class EmployeeSerializers(serializers.Serializer):
    empid = serializers.IntegerField()
    name = serializers.CharField(max_length=100)
    email = serializers.EmailField()
    password = serializers.IntegerField()