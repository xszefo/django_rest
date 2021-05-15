from django.urls import path
from . import views

urlpatterns = [
    path('', views.TaskListAPI.as_view(), name='TaskListAPI'),
]