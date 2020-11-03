from django.forms import ModelForm
from .models import Meeting
from django import forms

class MeetingCreationForm(ModelForm):
    time = forms.CharField(max_length=30, widget=forms.TimeInput(
        attrs={'placeholder': 'eg 8:00 enter the values according to 24 hour format'}))
    class Meta:
        model = Meeting
        fields = ['topic', 'subject', 'std', 'status', 'link', 'time']

