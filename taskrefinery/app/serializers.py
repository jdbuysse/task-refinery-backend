from rest_framework import serializers
from . import models
from django.contrib.auth.hashers import make_password


class SubtaskSerializer(serializers.ModelSerializer):
    task = serializers.ReadOnlyField(source='task.description')

    class Meta:
        model = models.Subtask
        #fields = ['id', 'content', 'task']
        fields = ('__all__')



class TaskSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    subtasks = SubtaskSerializer(many=True,read_only=True)
    
    class Meta:
        model = models.Task
        fields = ['id', 'title', 'description', 'owner', 'subtasks']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ('id', 'username', 'tasks', 'password')
        extra_kwargs = { 'password': {'write_only': True }}

    def create(self, validated_data):
        user = models.User.objects.create(
            #email = validated_data['email'],
            username = validated_data['username'],
            password = make_password(validated_data['password'])
        )
        user.save()
        return user