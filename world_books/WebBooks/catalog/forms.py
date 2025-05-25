from django import forms
from django.core.exceptions import ValidationError
from django.forms import SelectDateWidget

from .models import Task


class FormTask(forms.ModelForm):
    task = forms.CharField(max_length=20)
    status = forms.CharField(max_length=20)
    description = forms.CharField(max_length=20)
    date = forms.DateField(label='Срок:')
    class Meta:
        model = Task
        fields = ['task', 'status', 'description', 'date']