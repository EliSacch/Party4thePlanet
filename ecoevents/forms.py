from django.forms import ModelForm
from .models import Ecoevent, User
from django import forms


class EcoeventForm(ModelForm):
    """
    Form for creating and editing Ecoevents
    """
    class Meta:
        model = Ecoevent
        fields = [
            'title',
            'description',
            'category',
            'start_datetime',
            'end_datetime',
            'location'
            ]
        
        CHOICES = [
            ("Clean-up", "Clean-up"),
            ("Seminar", "Seminar"),
            ("Pop shop", "Pop shop"),
            ("Clothing swap", "Clothing swap"),
            ("Other", "Other"),
        ]
        widgets = {
            'start_datetime': forms.DateTimeInput(attrs={
                'type': 'datetime-local'}),
            'end_datetime': forms.DateTimeInput(attrs={
                'type': 'datetime-local'}),
            'category': forms.Select(choices=CHOICES)
        }


class UserForm(ModelForm):
    """
    Form for creating and editing Users
    """
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
