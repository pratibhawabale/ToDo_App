
from django.shortcuts import redirect, render

from .models import ToDo
from .forms import ToDoForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

# Create your views here.

def login_user(request):
    if request.user.is_authenticated: 
        return redirect("home")
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        try:
            user = User.objects.get(username=username)
        except:
            print("Error occured !!")
        
        user = authenticate(request, username = username, password = password) 
        # returns None if password not matched
        
        if user is not None:
            login(request, user)          #It will create session for this user in database
            			                #check inspect --> application --> cookies
            return redirect ("login")
        else:
            #messages.error(request,"Invalid username or password")
            print("Invalid username or password !!")
    return render(request,'to_do/login.html')

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