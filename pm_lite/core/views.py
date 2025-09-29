from rest_framework import viewsets, generics, permissions
from .models import Project, Task, Comment, User
from .serializers import UserSerializer, ProjectSerializer, TaskSerializer, CommentSerializer, RegisterSerializer
from rest_framework.permissions import IsAuthenticated


# ----------------------------------
# Project view Set
#-----------------------------------
class ProjectViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated] 
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

# ----------------------------------
# adding User view Set just to have an idea about list of users
#-----------------------------------
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]