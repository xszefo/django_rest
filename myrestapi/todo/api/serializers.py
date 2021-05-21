import todo.models as todo
from rest_framework import serializers

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        url = serializers.HyperlinkedIdentityField(view_name='api-todo:TaskDetailsAPI')
        model = todo.Task
        fields = ['id', 'title', 'url']


class TaskDetailSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()

    class Meta:
        model = todo.Task
        fields = ['id', 'title', 'username', 'deadline', 'created_at']

    def get_username(self, obj):
        return obj.user.username