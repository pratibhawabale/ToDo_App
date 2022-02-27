
from django.shortcuts import redirect, render

from .models import ToDo
from .forms import ToDoForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .forms import UserCreationForm
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url="login")
def logout_user(request):
    logout(request)
    return redirect("login")
    

def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid:
            user = form.save()
            login(request, user)
            return redirect("home")
        else:
            print("Error occured")

    user_form = UserCreationForm()
    context={"form": user_form}
    return render(request, "to_do/register_user.html", context)

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

@login_required(login_url="login")
def home(request):
    todos = ToDo.objects.all()
    context = {'todos': todos}
    return render(request,'to_do/home.html', context)

@login_required(login_url="login")
def add_todo(request):
    form = ToDoForm()
    context = {'form': form}
    if request.method == 'POST':
        form = ToDoForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('home') 
    return render(request, 'to_do/form.html', context)


@login_required(login_url="login")
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

@login_required(login_url="login")
def delete_todo(request, pk):
    todo = ToDo.objects.get(id=pk)
    if request.method == 'POST':
        todo.delete()
        return redirect('home')
    return render(request, 'to_do/delete.html')

@login_required(login_url="login")
def view_todo(request,pk):
    todo = ToDo.objects.get(id=pk)
    context = {'todo': todo}
    return render(request, 'to_do/todo.html', context)