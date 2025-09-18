from django.db import models 
from django.contrib.auth.models import User


# ----------------------------------
# My Project Model 
# Project Management Lite version
#-----------------------------------
class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Owned_projects')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


# ----------------------------------
# Project Member Model
# Project Management Lite version
#-----------------------------------
class ProjectMember(models.Model):
    role_choice = [ ("OWNER", "Owner"),("MEMBER", "Member"),]
    
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='project_name')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='project_membership')
    role = models.CharField(max_length=10, choices=role_choice, default='MEMBER')

    class Meta: 
        unique_together = ("project", "user")

    def __str__(self):
        return f"{self.user.username} - {self.role} in {self.project.name}"
    

# ----------------------------------
# Task Model
# Project Management Lite version
#-----------------------------------
class Task(models.Model):
    status_choice = [ ("TODO", "Todo"),("INPROGRESS", "InProgress"),("DONE", "Done"),]
    priority_choice = [ ("LOW", "low"),("MEDUIM", "Meduim"),("HIGH", "High"),]
    
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='project_name')
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=10, choices=status_choice, default='TODO')
    priority = models.CharField(max_length=10, choices=priority_choice, default='LOW')
    due_date = models.DateTimeField(blank=True, null=True)
    assignee = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='assigned_tasks')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_tasks')
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} ({self.status})"


# ----------------------------------
# Comment Model
# Project Management Lite version
#-----------------------------------
class Comment(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='task_comment')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_comment')
    text = models.TextField(blank=True ,null=True)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Comment by {self.author.username} on {self.task.title}"



