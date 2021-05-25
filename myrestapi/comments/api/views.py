from rest_framework.views import APIView
from rest_framework.response import Response

from comments.models import Comment
from .serializers import CommentSerializer, CommentDetailSerializer

class CommentListAPI(APIView):
    def get(self, request):
        context = {
            'request': request,
        }
        queryset =Comment.objects.all()
        serializer = CommentSerializer(queryset, many=True, context=context)
        return Response(serializer.data)

    # def post(self, request):
    #     context = {
    #         'request': request,
    #     }
    #     serializer = TaskSerializer(data=request.data, context=context)
		        
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 


