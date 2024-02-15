from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from .models import ToDoItem
from .forms import ToDoItemForm
import django.contrib.messages
import datetime

def show_home_page(request):
    global modifying_todo
    todos = ToDoItem.objects.all()
    if not todos.exists():
        todos = None
    return render(request, 'todo_home.html', {"todos": todos})

def create_todo(request):
    todo = None
    form = ToDoItemForm()
    if request.method == "POST":
        submitted_form = ToDoItemForm(request.POST)
        if submitted_form.is_valid():
            submitted_form.save()
            return redirect('../') #return to previous page ("todo_home.html")
        else:
            return HttpResponse("Invalid Input! return to the previous page to reinput")
    return render(request, 'todo_form.html', {"todo": todo, "form": form})

def modify_todo(request, pk): # pk: primary key (id of the model instance)
    modifying_todo = ToDoItem.objects.get(id=pk)
    form = ToDoItemForm(instance=modifying_todo)
    if request.method == 'POST':
        modified_form = ToDoItemForm(request.POST, instance=modifying_todo)
        if modified_form.is_valid():
            modified_form.save()
            return redirect('/todo')
        else:
            return HttpResponse("Invalid Input! return to the previous page to reinput")
        
    return render(request, "todo_form.html", {"todo": modifying_todo, "form": form})
    
def delete_todo(request, pk):
    deleting_todo = ToDoItem.objects.get(id=pk)
    if request.method == 'GET':
        deleting_todo.delete()
    return redirect('/todo')