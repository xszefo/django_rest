import todo.models as todo
from rest_framework import serializers

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = todo.Task
        fields = ['id', 'title', 'user', 'deadline', 'created_at']