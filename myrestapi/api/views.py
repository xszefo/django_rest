from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

import todo.models as todo
from .serializers import TaskSerializer

class TaskListAPI(APIView):
    def get(self, request):
        objects = todo.Task.objects.all()
        serializer = TaskSerializer(objects, many=True)
        return Response(serializer.data)