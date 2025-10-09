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
    #project = serializers.SlugRelatedField(slug_field='name', queryset=Project.objects.all())
    class Meta: 
        model = Task
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Comment
        fields = ['id', 'task', 'text', 'author', 'created_at']

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, min_length=6)
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')

    def create(self, validated_data):
        user = User.objects.create_user(username=validated_data["username"], email=validated_data.get("email",""), password=validated_data["password"])
        return user