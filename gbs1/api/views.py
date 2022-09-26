from django.shortcuts import render
from .models import Student
from .serializers import StudentSerilalizer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse,JsonResponse
# Create your views here.
def student_details(request, pk):
    stu = Student.objects.get(id=pk)
    #print(stu)
    serializer = StudentSerilalizer(stu)
    #print(serializer)
    #print(serializer.data)
    #json_data = JSONRenderer().render(serializer.data)
    #print(json_data)
    #return HttpResponse(json_data,content_type='application/json')
    return JsonResponse(serializer.data)

def student_list(request):
    stu = Student.objects.all()
    #print(stu)
    serializer = StudentSerilalizer(stu,many=True)
    #print(serializer)
    #print(serializer.data)
    json_data = JSONRenderer().render(serializer.data)
    #print(json_data)
    return HttpResponse(json_data,content_type='application/json')