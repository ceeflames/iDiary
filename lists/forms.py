from django import forms
from django.forms import ModelForm
from .models import Entry


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ('text',)
        widgets ={
            'text' : forms.Textarea(attrs={'placeholder':'what\'s on yor mind?'}),
        }
