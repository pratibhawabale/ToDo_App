
from django.shortcuts import redirect, render

from .models import ToDo
from .forms import ToDoForm


# Create your views here.

def home(request):
    todos = ToDo.objects.all()
    context = {'todos': todos}
    return render(request,'to_do/home.html', context)

def add_todo(request):
    form = ToDoForm()
    context = {'form': form}
    if request.method == 'POST':
        form = ToDoForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('home') 
    return render(request, 'to_do/form.html', context)


def update_todo(request, pk):
    todo = ToDo.objects.get(id=pk)
    form = ToDoForm(instance=todo)
    if request.method == 'POST':
        form = ToDoForm(request.POST, instance=todo)
        if form.is_valid:
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'to_do/form.html', context)

def delete_todo(request, pk):
    todo = ToDo.objects.get(id=pk)
    if request.method == 'POST':
        todo.delete()
        return redirect('home')
    return render(request, 'to_do/delete.html')

def view_todo(request,pk):
    todo = ToDo.objects.get(id=pk)
    context = {'todo': todo}
    return render(request, 'to_do/todo.html', context)