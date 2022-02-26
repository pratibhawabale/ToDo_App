from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('add-todo/', views.add_todo, name='add-todo'),
    path('update-todo/<str:pk>/', views.update_todo, name='update-todo'),
    path('view-todo/<str:pk>/', views.view_todo, name='view-todo'),
    path('delete-todo/<str:pk>/', views.delete_todo, name='delete-todo'),

    path('login/', views.login_user, name='login'),
]