from django.shortcuts import render, redirect
from .models import Ecoevent
from .forms import EcoeventForm
from django.contrib import messages
import json
from django.core import serializers
from django.http import JsonResponse


def home(request):
    return render(request, "index.html", {})


def events(request):
    all_events = Ecoevent.objects.all()
    category = request.GET.get("category")
    if category:
        events = all_events.filter(category=category)
    else:
        events = all_events
<<<<<<< HEAD
    context = {"events": events}
    return render(request, "events.html", context)
=======
    context = {'events': events}

    if request.method == 'POST':
        id = int(request.POST.get("id", ""))
        if id is not None:
            get_event = Ecoevent.objects.filter(id=id)
            selected_event = serializers.serialize('json', get_event,)

        return JsonResponse({'selected_event': selected_event})

    return render(request, 'events.html', context)
>>>>>>> 72459bb85030f25ce8cb87a713a6ea6360a81c6f


def event(request, event_id):
    event = Ecoevent.objects.get(pk=event_id)
    context = {"event": event}
    return render(request, "event.html", context)


def map(request):
    context = {}
    return render(request, "map.html", context)


def profile(request):
    context = {}
    return render(request, "profile.html", context)


def createEvent(request):
    form = EcoeventForm()

    if request.method == "POST":
        form = EcoeventForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Event created successfully!")
            return redirect("events")

    context = {"form": form}
    return render(request, "event_form.html", context)
