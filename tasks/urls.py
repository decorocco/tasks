from django.urls import path

from views import index, listTask,postTask,deleteTask

urlpatterns = [
    path('', index, name='index'),
    path('get', listTask, name='getTasks'),
    path('post',postTask, name='postTask'),
    path('delete/<int:id>',deleteTask,name='deleteTask')
]
