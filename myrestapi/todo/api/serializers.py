import todo.models as todo
from rest_framework import serializers

class TaskSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='api-todo:TaskDetailsAPI', lookup_field = 'pk')
    number_of_comments = serializers.SerializerMethodField()

    class Meta:
        model = todo.Task
        fields = ['id', 'title', 'url', 'number_of_comments']
    
    def get_number_of_comments(self, obj):
        try:
            return obj.comment_set.count()
        except AttributeError:
            return 0

class TaskDetailSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()
    class Meta:
        model = todo.Task
        fields = ['id', 'title', 'username', 'deadline', 'created_at']

    def get_username(self, obj):
        try:
            return obj.user.username
        except AttributeError:
            return None