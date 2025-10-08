from rest_framework import viewsets, generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Project, Task, Comment, User
from .serializers import UserSerializer, ProjectSerializer, TaskSerializer, CommentSerializer, RegisterSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import IsProjectOwnerOrReadOnly, IsProjectMember



# ----------------------------------
# Project view Set
#-----------------------------------
class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated, IsProjectOwnerOrReadOnly] 
    def get_queryset(self):
        user = self.request.user
        # projects owned by user OR where user is a member
        owned = Project.objects.filter(owner=user)
        member = Project.objects.filter(projectmember__user=user) 
        return (owned | member).distinct()


# ----------------------------------
# Task view Set
#-----------------------------------
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated, IsProjectMember] 
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    # Which fields can be filtered
    filterset_fields = ['status', 'priority', 'assignee']
    # Which fields can be searched with ?search= keyword
    search_fields = ['title', 'assignee']
    # Which fields can be used for ordering
    ordering_fields = ['created_at', 'status', 'priority']
    # default ordering
    ordering = ['created_at']

    def get_queryset(self):
        user = self.request.user
        return Task.objects.filter(project__owner=user) | Task.objects.filter(project__memberships__user=user)





# ----------------------------------
# Comment view Set
#-----------------------------------
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

# ----------------------------------
# adding User view Set just to have an idea about list of users
#-----------------------------------
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]