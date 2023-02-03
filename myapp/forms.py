from django import forms

class CreateNewTask(forms.Form):
    title = forms.CharField(label="Title of task", max_length=200)
    description = forms.CharField(label="Description of the taks", widget=forms.Textarea)