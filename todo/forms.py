from django import forms
from .models import ToDoItem

class ToDoItemForm(forms.ModelForm):
    class Meta:
        model = ToDoItem
        # exclude = ['is_urgent', 'modifying']
        fields = ['title', 'due_date', 'completed']