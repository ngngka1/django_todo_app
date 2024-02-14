from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from .models import ToDoItem
from .forms import ToDoItemForm
import django.contrib.messages
import datetime

modifying_todo = None

def show_home_page(request):
    global modifying_todo
    todos = ToDoItem.objects.all()
    if not todos.exists():
        todos = []
        
    if request.method == 'POST':
        modifiying_todo_title = request.POST.get('modifying_todo_title')
        modifying_todo = ToDoItem.objects.get(title=modifiying_todo_title) # will be changed
        # when i know how to pass arguments to views through redirect
        return redirect(modify_todos)
    else:
        return render(request, 'todo_home.html', {"todos": todos})

def create_todo(request):
    if request.method == 'POST':
        form = ToDoItemForm(request.POST)
        if form.is_valid():
            form.save(True)
            return redirect('../')
        else:
            # django.contrib.messages.info(request, "Invalid input!")
            return HttpResponse("Invalid Input")
    else:
        form = ToDoItemForm()
        return render(request, "manage_todos.html", {"todo": None, "current_date": datetime.date.today, "form": form})      

def modify_todos(request):
    if request.method == 'POST':
        form = ToDoItemForm(request.POST, instance=modifying_todo)
        if form.is_valid():
            form.save()
            return redirect('../')
        else:
            # django.contrib.messages.info(request, "Invalid input!")
            return HttpResponse("Invalid Input")
    else:
        form = ToDoItemForm(instance=modifying_todo)
        return render(request, "manage_todos.html", {"todo": modifying_todo, "current_date": datetime.date.today, "form": form})
    
def delete_todos(request):
    if request.method == 'POST':
        modifying_todo.delete()