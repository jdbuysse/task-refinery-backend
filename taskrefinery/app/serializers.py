from rest_framework import serializers
from . import models

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Task
        fields = ['id', 'title', 'description']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ('id', 'username', 'email')