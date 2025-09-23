from rest_framework import serializers
from .models import Project, ProjectMember, Task, Comment
from django.contrib.auth.models import User



class UserSerializer(serializers.ModelSerializer):
    class Meta: 
        model = User
        fields = ['id', 'username', 'email']

class ProjectSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Project
        fields = ['id', 'name', 'description', 'owner', 'created_at']       

class TaskSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Task
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Comment
        fields = ['id', 'task', 'text', 'author', 'created_at']