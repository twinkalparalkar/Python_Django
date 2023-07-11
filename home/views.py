# from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET','POST','PATCH'])#API decoretor
def home(request):
    response={'status':200,'message':"hi,I am DRF"}
    if request.method=="POST":
        print('POST')
    elif request.method=="GET":
        print('GET')
    return Response(response)


