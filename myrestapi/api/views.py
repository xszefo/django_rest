from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

import todo.models as todo
from .serializers import TaskSerializer

class TaskListAPI(APIView):
    def get(self, request):
        objects = todo.Task.objects.all()
        serializer = TaskSerializer(objects, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TaskSerializer(data=request.data)
		
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)