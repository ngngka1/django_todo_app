from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializer import ToDoItemSerializer
from todo.models import ToDoItem

def show_home_page(request):
    return render(request, "todo_api_home.html")

@api_view(['GET'])
def get_data(request, pk=None):
    if pk is None:
        todos = ToDoItem.objects.all()
    else:
        todos = ToDoItem.objects.filter(id=pk)
        if not todos.exists():
            return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = ToDoItemSerializer(todos, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def add_data(request):
    serializer = ToDoItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT'])
def modify_data(request, pk):
    if not ToDoItem.objects.filter(id=pk).exists(): # Check if the instance queryset is empty, if is empty, the item does not exist
        return Response(status=status.HTTP_404_NOT_FOUND)
    else:
        modifying_todo = ToDoItem.objects.get(id=pk)
        serializer = ToDoItemSerializer(modifying_todo, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'DELETE'])
def delete_data(request, pk):
    if not ToDoItem.objects.filter(id=pk).exists():
        return Response(status=status.HTTP_404_NOT_FOUND)
    else:
        deleting_todo = ToDoItem.objects.get(id=pk)
        deleting_todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
    
