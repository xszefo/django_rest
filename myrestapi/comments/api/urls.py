from django.urls import path
from . import views

app_name = 'todo'
urlpatterns = [
    path('', views.CommentListAPI.as_view(), name='CommentsListAPI'),
    #path('<int:pk>', views.CommentDetailsAPI.as_view(), name='CommentsDetailsAPI'),

]