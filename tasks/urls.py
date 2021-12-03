from django.urls import path

from views import index, listTask,postTask,deleteTask

urlpatterns = [
    path('', views.index, name='index'),
]
