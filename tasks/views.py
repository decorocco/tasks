from django.db.models import query
from rest_framework import viewsets
from .models import Task
from .serializer import TaskSerializer

# def index(request):
#     all_tasks = Task.objects.all()
#     return HttpResponse(all_tasks)

class TasksViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
