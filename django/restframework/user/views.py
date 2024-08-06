from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
'''from .serializer import *
from .models import *

@api_view(['GET'])
def getall(request):
    stdata=stude_info.objects.all()
    serial=stude(stdata,many=True)
    return Response(data=serial.data,status=status.HTTP_200_OK)


@api_view(['GET'])
def getstid(request,id):
    try:
        stid=stude_info.objects.get(id=id)
    except stude_info.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serial=stude_info(stid)
    return Response(data=serial.data,status=status.HTTP_200_OK)'''