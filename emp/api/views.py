from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.
from .models import Employee
from .serializers import EmployeeSerializers
from requests import Response

@api_view(['GET','POST'])
def Employee_api(request,pk=None):
    # if request.mothod == 'GET':
    #     id = pk
    #     if id is not None:
    #         emp = Employee
    if request.method == 'POST':
        serializer = EmployeeSerializers(data=request.data)
        if serializer.is_valid():
            
            return Response({'msg':'Recored is Match'})
        return Response(serializer.errors)
