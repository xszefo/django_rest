from django.urls import path
from . import views

urlpatterns = [
    path('', views.TaskListAPI.as_view(), name='TaskListAPI'),
    path('<int:id>', views.TaskDetailsAPI.as_view(), name='TaskDetailsAPI'),

]