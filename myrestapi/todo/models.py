from django.db import models
from django.conf import settings

class Task(models.Model):
    title = models.CharField(max_length=50)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    deadline = models.DateTimeField(auto_now=False, auto_now_add=False, null=True, blank=False)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.title