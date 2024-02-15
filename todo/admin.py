from django.contrib import admin
from .models import ToDoItem, Subject

# Register your models here.
admin.site.register(ToDoItem)
admin.site.register(Subject)