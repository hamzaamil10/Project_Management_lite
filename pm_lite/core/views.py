from rest_framework import viewsets
from .models import Project, Task, Comment, User
from .serializers import UserSerializer, ProjectSerializer, TaskSerializer, CommentSerializer


# ----------------------------------
# Project view Set
#-----------------------------------
class ProjectViewSet(viewsets.ModelViewSet): 
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


# ----------------------------------
# Task view Set
#-----------------------------------
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


# ----------------------------------
# Comment view Set
#-----------------------------------
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer