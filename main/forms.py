from django.forms import ModelForm
from .models import Meeting

class MeetingCreationForm(ModelForm):
    class Meta:
        model = Meeting
        fields = ['topic', 'subject', 'std', 'status', 'link', 'time']

