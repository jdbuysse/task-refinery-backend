from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.
class Task(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    description = models.CharField(max_length=200)

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='tasks', on_delete=models.CASCADE, default=0)

    class Meta:
        ordering = ['created']

    def save(self, *args, **kwargs):
        options = {'title': self.title} if self.title else {}
        super(Task, self).save(*args, **kwargs)

class Subtask(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    content = models.CharField(max_length=200)
    #data = models.JSONField(type=dict, default={}) probably have to do something like this

    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name="subtasks") #add these? , null=True, blank=True
    completedness = models.IntegerField(default='1')

    class Meta:
        ordering = ['created']

    def __str__(self):
        return self.content

# essentially the same as importing User above
class User(AbstractUser):

    def __str__(self):
        return self.username
