from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import *

# Create your views here.

@api_view(['GET'])
def getall(requset):
    data=book.objects.all()
    serial=books(data,many=True)
    return Response(data=serial.data,status=status.HTTP_200_OK)

@api_view(['GET'])
def getstid(request,id):
    try:
        stid=book.objects.get(id=id)
    except book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serial=books(stid)
    return Response(data=serial.data,status=status.HTTP_200_OK)