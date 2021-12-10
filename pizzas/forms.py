from django import forms

from .models import Pizza, Comment

class TopicForm(forms.ModelForm):
    class Meta:
        model = Pizza
        fields = ['name']
        labels = {'name':''}

class EntryForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name']
        labels = {'name': ""}