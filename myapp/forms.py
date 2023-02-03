from django import forms
from .models import Project

class CreateNewTask(forms.Form):
    title = forms.CharField(label="Title of task", max_length=200, widget=forms.TextInput(attrs={'class' : 'input'}))
    description = forms.CharField(label="Description of the taks", widget=forms.Textarea(attrs={'class': 'input'}))
    project_id = forms.ModelChoiceField(queryset=Project.objects.all(), required=True)

class CreateNewForm(forms.Form):
    name = forms.CharField(label="Name of Project", max_length=200, widget=forms.TextInput(attrs={'class': 'input'}))