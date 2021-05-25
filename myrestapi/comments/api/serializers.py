#import comments.models as comments
from comments.models import Comment
from rest_framework import serializers

from todo.api.serializers import TaskDetailSerializer

class CommentSerializer(serializers.ModelSerializer):
    #url = serializers.HyperlinkedIdentityField(view_name='api-comments:CommentsDetailsAPI', lookup_field = 'pk')
    username = serializers.SerializerMethodField()
    task = TaskDetailSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'content', 'username', 'task']#, 'url']

    def get_username(self, obj):
        return obj.user.username

    def get_task_title(self, obj):
        return obj.task.title

class CommentDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'user', 'content', 'created_at', 'updated_at']
