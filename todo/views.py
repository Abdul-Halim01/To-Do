from django.shortcuts import render
from todo_app.models import Task

def home(request):
    tasks = Task.objects.filter(is_completed=False).order_by('-updated_at')
    completed_tasks = Task.objects.filter(is_completed=True).order_by('-updated_at')
    context= {
        'tasks':tasks,
        'completed_tasks':completed_tasks,
    }
    print(completed_tasks)
    return render(request,'home-todo.html',context)
