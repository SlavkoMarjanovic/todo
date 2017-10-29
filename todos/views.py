from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.views.generic import TemplateView, ListView
from .models import Todo
from  .serializers import TodoSerializers
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.

def index(request):
    todos = Todo.objects.all()
    context = {
        'todos': todos
    }
    return render(request, 'index.html', context)
def details(request, id):
    todo = Todo.objects.get(id = id)
    context = {
        'todo': todo
    }
    return render(request, 'details.html', context)
def add(request):
    if (request.method == 'POST'):
        title = request.POST['title']
        text = request.POST['text']
        todo =Todo(title= title, text= text)
        todo.save()
        return redirect('/todos')
    else:
        return render(request, 'add.html')
class TodoList(APIView):
    def get(self,request):
        todo1 = Todo.objects.all()
        serializer = TodoSerializers(todo1, many=True)
        return Response(serializer.data)

    def post(self):
        pass