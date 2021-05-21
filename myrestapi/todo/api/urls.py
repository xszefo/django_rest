from django.urls import path
from . import views

app_name = 'todo'
urlpatterns = [
    path('', views.TaskListAPI.as_view(), name='TaskListAPI'),
    path('<int:pk>', views.TaskDetailsAPI.as_view(), name='TaskDetailsAPI'),

]