from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import NotFound

import todo.models as TODO
from .serializers import TaskSerializer, TaskDetailSerializer
from .pagination import TaskPaginationPage

# class TaskListAPI(generics.ListAPIView):
#     queryset = TODO.Task.objects.all()
#     pagination_class = TaskPaginationPage
#     serializer_class = TaskSerializer
    
class TaskListAPI(APIView):
    def get(self, request):
        context = {
            'request': request,
        }
        pagination_class = TaskPaginationPage
        queryset = TODO.Task.objects.all()
        serializer = TaskSerializer(queryset, many=True, context=context)
        return Response(serializer.data)

    def post(self, request):
        context = {
            'request': request,
        }
        serializer = TaskSerializer(data=request.data, context=context)
		        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)        

class TaskDetailsAPI(APIView):
    def get_object(self, pk):
        try:
            return TODO.Task.objects.get(pk=pk)
        except:
            raise NotFound(detail="Error 404, object not found", code=404)

    def get(self, request, pk):
        obj = self.get_object(pk)
        obj_json = TaskDetailSerializer(obj)
        return Response(obj_json.data)

    def put(self, request, pk):
        context = {
            'request': request,
        }
        obj = self.get_object(pk)
        serializer = TaskSerializer(obj, data=request.data, context=context)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)   

    def delete(self, request, pk):
        obj = self.get_object(pk)
        obj.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
