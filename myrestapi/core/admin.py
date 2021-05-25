from django.contrib import admin
from todo.models import Task
from comments.models import Comment
# Register your models here.

admin.site.register(Task)
admin.site.register(Comment)