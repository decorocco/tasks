from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from tasks.serializer import TaskSerializer
from tasks.models import Task
import django

# Create your views here.


def index(request):
    return HttpResponse("Hello, world. You're at the tasks index.")

@api_view(['GET'])
def taskList(request):
    django.middleware.csrf.get_token(request)
    if request.method == 'GET':
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        print("GET feito")
        return HttpResponse(JsonResponse( serializer.data,safe=False))
    if request.method == 'POST':
        return render(request,'forms.html')
def taskDelete(request, id):
    tasks = Task.objects.get(id=id)
    tasks.delete()
    print("DELETE Efetuado")
    return HttpResponse(JsonResponse({'data':'ok'},safe=False))
def taskPost(request):
    if request.method == "POST":  
        form = TaskSerializer(data=request.POST)
        if form.is_valid():  
            try:  
                form.save()  
                print("POST feito")
                return HttpResponse(JsonResponse({'data':'ok'},safe=False))
            except Exception as e: 
                return HttpResponse(JsonResponse({'data':e},safe=False))
        else:
            return HttpResponse(JsonResponse({'data':'error'},safe=False))
    else:
        return render(request,'forms.html')
