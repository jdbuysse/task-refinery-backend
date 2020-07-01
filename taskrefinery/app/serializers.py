from rest_framework import serializers
from . import models
from django.contrib.auth.hashers import make_password

class TaskSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = models.Task
        fields = ['id', 'title', 'description', 'owner']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ('id', 'username', 'tasks')
        extra_kwargs = { 'password': {'write_only': True }}

    def create(self, validated_data):
        user = models.User.objects.create(
            #email = validated_data['email'],
            username = validated_data['username'],
            password = make_password(validated_data['password'])
        )
        user.save()
        return user