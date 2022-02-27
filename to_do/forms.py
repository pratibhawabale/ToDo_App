from django.forms import ModelForm
from .models import ToDo
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User

class ToDoForm(ModelForm):
    class Meta:
        model = ToDo
        fields = '__all__'

class  CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["first_name", "email", "username", "password1", "password2"]
        labels={
            "first_name": "name",
        }
