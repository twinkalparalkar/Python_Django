# from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view()#API decoretor
def home(request):
    response={'status':200,'message':"hi,I am DRF"}
    return Response(response)
