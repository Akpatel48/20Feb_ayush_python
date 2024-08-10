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

@api_view(['GET','DELETE'])
def deleteid(requset,id):
    try:
        id=book.objects.get(id=id)
    except book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if requset.method=='GET':
        serial=books(id)
        return Response(data=serial.data,status=status.HTTP_200_OK)
    
    if requset.method=='DELETE':
        book.delete(id)
        return Response(status=status.HTTP_202_ACCEPTED)

@api_view(['POST'])
def insertdata(request):
    if request.method=='POST':
        serial=books(data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT'])
def update(request,id):
    try:
        id=book.objects.get(id=id)
    except book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method=='GET':
        serial=books(id)
        return Response(data=serial.data,status=status.HTTP_200_OK)
    
    if request.method=='PUT':
        serial=books(data=request.data,instance=id)
        if serial.is_valid():
            serial.save()
            return Response(status=status.HTTP_202_ACCEPTED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)   