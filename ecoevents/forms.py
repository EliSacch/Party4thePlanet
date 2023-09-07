from django.forms import ModelForm
from .models import Ecoevent
from django import forms


class EcoeventForm(ModelForm):
    """
    Form for creating and editing Ecoevents
    """
    class Meta:
        model = Ecoevent
        fields = [
            'organizer',
            'title',
            'description',
            'category',
            'start_datetime',
            'end_datetime',
            'location'
            ]
        widgets = {
            'start_datetime': forms.DateTimeInput(attrs={
                'type': 'datetime-local'}),
            'end_datetime': forms.DateTimeInput(attrs={
                'type': 'datetime-local'}),
        }
