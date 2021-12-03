from django.db.models import query
from rest_framework import viewsets
from .models import Task
from .serializer import TaskSerializer

class TasksViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
