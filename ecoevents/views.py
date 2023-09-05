from django.shortcuts import render
from .models import Ecoevent


def home(request):
    return render(request, 'index.html', {})


def events(request):
    all_events = Ecoevent.objects.all
    context = {'all_events': all_events}
    return render(request, 'events.html', context)