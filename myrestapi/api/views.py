from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

import todo.models as TODO
from .serializers import TaskSerializer, TaskDetailSerializer

class TaskListAPI(APIView):
    def get(self, request):
        objects = TODO.Task.objects.all()
        serializer = TaskSerializer(objects, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TaskSerializer(data=request.data)
		
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TaskDetailsAPI(APIView):
    def get_object(self, id):
        try:
            return TODO.Task.objects.get(id=id)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        obj = self.get_object(id)
        obj_json = TaskDetailSerializer(obj)
        return Response(obj_json.data)
