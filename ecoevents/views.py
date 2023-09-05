from django.shortcuts import render
from .models import Ecoevent


def home(request):
    return render(request, 'index.html', {})


def events(request):
    all_events = Ecoevent.objects.all
    context = {'all_events': all_events}
    return render(request, 'events.html', context)


def event(request, event_id):
    event = Ecoevent.objects.get(pk=event_id)
    context = {'event': event}
    return render(request, 'event.html', context)


def map(request):
    context = {}
    return render(request, 'map.html', context)
