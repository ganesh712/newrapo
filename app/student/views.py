from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.views import APIView
# Create your views here.
from django.http import HttpResponse,response
def home(request):
    return HttpResponse("Hello World")
@api_view(['GET'])
def studentapi(APIview):
    if request.method=='GET':
        print(request.data)
        return Response({"msg" : "Hello world api"})
    
    

    
   
