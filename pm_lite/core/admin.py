from django.contrib import admin
from .models import Project, ProjectMember, Task, Comment


# --------------------
# Inline for ProjectMember
# --------------------
class ProjectMemberInline(admin.TabularInline):
    model = ProjectMember
    extra = 1  # how many blank rows to show
    autocomplete_fields = ["user"]


# --------------------
# Project Admin
# --------------------
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("name", "owner", "created_at")
    search_fields = ("name", "description", "owner__username")
    inlines = [ProjectMemberInline]


# --------------------
# Task Admin
# --------------------
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("title", "project", "status", "priority", "assignee", "due_date", "created_by")
    list_filter = ("status", "priority", "project")
    search_fields = ("title", "description", "assignee__username", "project__name")
    autocomplete_fields = ["project", "assignee", "created_by"]


# --------------------
# Comment Admin
# --------------------
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("task", "author", "created_at")
    search_fields = ("text", "author__username", "task__title")
    autocomplete_fields = ["task", "author"]


# --------------------
# ProjectMember Admin (optional, since it's inline already)
# --------------------
@admin.register(ProjectMember)
class ProjectMemberAdmin(admin.ModelAdmin):
    list_display = ("project", "user", "role")
    list_filter = ("role", "project")
    search_fields = ("user__username", "project__name")