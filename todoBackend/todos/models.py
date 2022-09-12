from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Todo(models.Model):
    created = models.DateField(auto_now_add=True)
    todo = models.CharField(max_length=100, null=False, blank=False)
    completed = models.BooleanField(default=False)
    owner = models.ForeignKey(User, related_name='todos', on_delete=models.CASCADE)

    def __str__(self):
        return self.todo
