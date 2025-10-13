from rest_framework import viewsets, generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Project, Task, Comment, User, ProjectMember
from .serializers import UserSerializer, ProjectSerializer, TaskSerializer, CommentSerializer, RegisterSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import IsProjectOwnerOrReadOnly, IsProjectMember
from django.shortcuts import render, get_object_or_404
from django.db.models import Q



# ----------------------------------
# Project view Set
#-----------------------------------
class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated, IsProjectOwnerOrReadOnly] 
    def get_queryset(self):
        user = self.request.user
        return Project.objects.filter(Q(owner=user) | Q(memberships__user=user)).distinct()
        # projects owned by user OR where user is a member
        #owned = Project.objects.filter(owner=user)
        #member = Project.objects.filter(project_memberships__user=user) 
        #return (owned | member).distinct()


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
    search_fields = ['title', 'assignee__username', 'assignee__email']
    # Which fields can be used for ordering
    ordering_fields = ['created_at', 'status', 'priority']
    # default ordering
    ordering = ['created_at']

    def get_queryset(self):
        user = self.request.user
        if not user.is_authenticated:
            return Task.objects.none()
        qs = Task.objects.filter(
        Q(project__owner=user) | Q(project__memberships__user=user)).distinct()

        project_param = self.request.query_params.get('project')
        if project_param:
            if project_param.isdigit():
                qs = qs.filter(project_id=int(project_param))
            else:
                qs = qs.filter(Q(project__slug=project_param) | Q(project__name=project_param))

        return qs





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


def home(request):
    return render(request, 'core/index.html')

def project_list(request):
    projects = Project.objects.all()
    return render(request, 'core/projects.html', {'projects': projects})

def project_detail(request, pk):
    project = get_object_or_404(Project.objects.select_related('owner'), pk=pk)

    # Optional access control (you can remove this block if not needed)
    is_member = request.user.is_authenticated and (
        project.owner_id == request.user.id or
        ProjectMember.objects.filter(project=project, user=request.user).exists()
    )
    if not is_member:
        return render(request, "core/not_allowed.html", status=403)

    tasks = (
        Task.objects.filter(project=project)
        .select_related('assignee', 'created_by')
        .order_by('-updated_at')
    )
    return render(request, "core/project_detail.html", {"project": project, "tasks": tasks})


def task_detail(request, pk):
    task = get_object_or_404(
        Task.objects.select_related('project', 'assignee', 'created_by'),
        pk=pk
    )

    # Optional access control
    is_member = request.user.is_authenticated and (
        task.project.owner_id == request.user.id or
        ProjectMember.objects.filter(project=task.project, user=request.user).exists()
    )
    if not is_member:
        return render(request, "core/not_allowed.html", status=403)

    comments = Comment.objects.filter(task=task).select_related('author').order_by('-created_at')
    return render(request, "core/task_detail.html", {"task": task, "comments": comments})