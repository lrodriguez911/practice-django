from django import forms

class CreateNewTask():
    title = forms.CharField(label="Title Of task", max_length=200)
    description = forms.Textarea(required=False)