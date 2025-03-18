from django import forms
from .models import Task

class DateInput(forms.DateInput):
    input_type = 'date'

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date', 'status']
        widgets = {
            'due_date': DateInput(),
            'description': forms.Textarea(attrs={'rows': 4, 'cols': 40, 'placeholder': 'Enter task description here...'}),
        }