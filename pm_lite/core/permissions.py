from rest_framework import permissions
from .models import ProjectMember

"""
    Only the owner can update/delete the project.
    Read access allowed for authenticated project members.
    """

class IsProjectOwnerOrReadOnly(permissions.BasePermission):
    # To allow if user is project member or owner using SAFE_METHODS
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            if obj.owner == request.user:
                return True
            return ProjectMember.objects.filter(project=obj, user=request.user).exists
        return obj.owner == request.user
    

"""
    Permission ensuring the user is a member of the related project.
    For object-level checks, expects obj to be a Task (has project attr).
    For list or create, we allow authenticated users but views should filter properly.
    """
class IsProjectMember(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        project = getattr(obj, "project", obj) if hasattr(obj, "project") else obj
        if hasattr(obj,"project"):
            project=obj.project
        else:
            project=obj
        
        if project.owner == request.user:
            return True
        return ProjectMember.objects.filter(project=project, user=request.user).exists
