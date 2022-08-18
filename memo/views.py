from django.shortcuts import render
from rest_framework.decorators import api_view
from .serializer import MemoSerializer
from rest_framework import viewsets, permissions, generics, status
from rest_framework.response import Response
from .models import Memo
# Create your views here.


@api_view(['POST'])
def createMemo(request):
    try:
        print(request.user)
        today=Memo.objects.get(  username=request.user )
        today.content=request.data["content"]
        today.save()
        return Response("ok!",status=200)
    except:
        serializer=MemoSerializer(data=request.data)
        if(serializer.is_valid()):
            serializer.save(username=request.user)
            print(request.user)
            print("Memo set:",serializer.data)
                
            return Response("ok!",status=200)
        
        return Response(serializer.errors ,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def getMemo(request):
    try:
        today=Memo.objects.get(username=request.user)
        serializer= MemoSerializer(today)
        return Response(serializer.data,status=200)
    except:
        return Response("Not found error",status=status.HTTP_404_NOT_FOUND)