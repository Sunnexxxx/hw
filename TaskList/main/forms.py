from django import forms
from main.models import *


class AddTaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ('title', 'description', 'priority', 'deadline', 'status', 'image')
        widgets = {
            'deadline': forms.TextInput(attrs={'type': 'datetime-local'})
        }


class SettingsForm(forms.Form):
    theme = forms.ChoiceField(choices=(('Dark', 'Dark'), ('Light', 'Light')))
    clear_history = forms.BooleanField(required=False)
    clean_actions = forms.BooleanField(required=False)
    sorted_by = forms.ChoiceField(choices=(('Title', 'Title'), ('Deadline', 'Deadline'),
                                           ('Priority', 'Priority')))
