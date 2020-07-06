from . import models
from app.serializers import TaskSerializer, UserSerializer, SubtaskSerializer

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics, mixins, viewsets, permissions
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse

# @api_view(['GET'])
# def api_root(request, format=None):
#     return Response({
#         'users': reverse('user-list', request=request, format=format),
#         'tasks': reverse('task-list', request=request, format=format)
#     })

class UsersList(generics.ListCreateAPIView): #should this allow create as well as list?
    queryset = models.User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]

class CreateUser(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

class UserDetail(generics.RetrieveAPIView):
    queryset = models.User.objects.all()
    serializer_class = UserSerializer
    #permission_classes = [permissions.]


class TaskList(generics.ListCreateAPIView):
    queryset = models.Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    # def patch(self, request, pk):
    #     obj = self.get_object(pk)
    #     serializer = TaskSerializer(obj, data=request.data, partial=True)


class SubtaskList(generics.ListCreateAPIView):
    queryset = models.Subtask.objects.all()
    serializer_class = SubtaskSerializer
    permission_classes= [permissions.AllowAny]

    