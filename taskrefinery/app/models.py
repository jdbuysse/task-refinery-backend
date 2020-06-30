from django.db import models
from django.contrib.auth.models import User, AbstractUser


# Create your models here.
class Task(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    description = models.CharField(max_length=200)

    class Meta:
        ordering = ['created']


class User(AbstractUser):

    def __str__(self):
        return self.username
