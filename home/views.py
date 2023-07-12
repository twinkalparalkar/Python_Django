# from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializer import *
@api_view(['GET'])#API decoretor
def get_students(request):
    response={'status':200,'message':"hi,I am DRF"}
    student_objs=Student.objects.all()
    serializer=StudentSerializer(student_objs,many=True)
    response['data']=serializer.data
    return Response(response)

@api_view(['POST'])#API decoretor
def post_students(request):
    response={'status':200,'message':"hi,I am DRF"}
    data=request.data
    serializer=StudentSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(response)
    return Response(serializer.errors)

@api_view(['GET','POST','PATCH'])#API decoretor
def home(request):
    response={'status':200,'message':"hi,I am DRF"}
    if request.method=="POST":
        print('POST')
    elif request.method=="GET":
        print('GET')
    return Response(response)


