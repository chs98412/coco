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
        memo=Memo.objects.get(  username=request.user )#minjoon
        memo.content=request.data["content"]
        memo.save()
        return Response("ok!",status=200)


    except:
        serializer=MemoSerializer(data=request.data)
        if(serializer.is_valid()):#무조건 있어야 하는 문장
            serializer.save(username=request.user)#minjoon
            print(request.user)
            print("Memo set:",serializer.data)
            
            return Response("ok!",status=200)
        
        return Response(serializer.errors ,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def getMemo(request):
    try:
        memo=Memo.objects.get(username=request.user)# 딱 하나!
        serializer= MemoSerializer(memo)
        return Response(serializer.data,status=200)
    except:
        return Response("Not found error",status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def createMemos(request):
    
        serializer=MemoSerializer(data=request.data)
        if(serializer.is_valid()):#무조건 있어야 하는 문장
            serializer.save(username=request.user)#minjoon
            print(request.user)
            print("Memo set:",serializer.data)
            
            return Response("ok!",status=200)
        
        return Response(serializer.errors ,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def getMemos(request):
    try:
        memo=Memo.objects.filter(username=request.user)# 조건에 부합하는 메모 모두!
        serializer= MemoSerializer(memo,many=True)
        return Response(serializer.data,status=200)
    except:
        return Response("Not found error",status=status.HTTP_404_NOT_FOUND)

