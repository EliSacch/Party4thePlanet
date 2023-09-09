import os
import requests
import datetime
import json  # noqa

from .models import Ecoevent
from .forms import EcoeventForm, UserForm

from django.shortcuts import render, redirect
from django.core import serializers
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth.models import User

from urllib.parse import urlencode
from .utils import extract_coordinates

def home(request):
    return render(request, "index.html", {})


def events(request):
    now = datetime.datetime.now()
    all_events = Ecoevent.objects.all().filter(start_datetime__gte=now)
    all_categories = []

    # Retrieve all categories
    for event in all_events:
        if event.category not in all_categories:
            all_categories.append(event.category)

    # filter
    category = request.GET.get("category")
    if category:
        events = all_events.filter(category=category)
    else:
        events = all_events
    
    # context
    context = {"events": events,
               "all_categories": all_categories,
               "category": category
               }
    
    # Dynamically get event and display card content
    if request.method == "POST":
        id = int(request.POST.get("id", ""))
        if id is not None:
            event = Ecoevent.objects.filter(id=id)
            organizer = event[0].organizer.username

            selected_event = serializers.serialize(
                "json",
                event,
            )
        return JsonResponse({
            "selected_event": selected_event,
            "organizer": organizer
            })

    return render(request, "events.html", context)


def event(request, event_id):
    event = Ecoevent.objects.get(pk=event_id)
    context = {"event": event}
    return render(request, "event.html", context)


def map(request):
    now = datetime.datetime.now()
    all_events = Ecoevent.objects.all().filter(start_datetime__gte=now)

    events = []
    categories = []
    all_categories = []
    for event in all_events:
        if event.category not in all_categories:
            all_categories.append(event.category)
    category = request.GET.get("category")
    if category:
        all_events = all_events.filter(category=category)

    for event in all_events:
        try:
            events.append({
                "title": event.title,
                "coordinates": extract_coordinates(event.location)
            })
        except:
            pass
        categories.append(event.category)

    context = {
        "events": json.dumps(events),
        "categories": categories,
        'all_categories': all_categories,
    }
    return render(request, "map.html", context)


def profile(request):
    my_events = Ecoevent.objects.filter(organizer=request.user)
    context = {
        "my_events": my_events,
    }
    return render(request, "profile.html", context)


def createEvent(request):
    form = EcoeventForm()
    user = request.user

    if request.method == "POST":
        form = EcoeventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)

            # check if location is valid
            location = form.cleaned_data.get('location')
            if extract_coordinates(location) == (None, None):
                messages.error(request, f"Invaid location: {location}")
            else:
                event.organizer = user
                event.save()
                form.save()
                messages.success(request, "Event created successfully")
                return redirect("events")

    context = {"form": form}
    return render(request, "event_form.html", context)


def editEvent(request, event_id):
    event = Ecoevent.objects.get(pk=event_id)
    form = EcoeventForm(instance=event)
    if request.user == event.organizer:
        if request.method == "POST":
            form = EcoeventForm(request.POST, instance=event)
            if form.is_valid():

                # check if location is valid
                location = form.cleaned_data.get('location')
                if extract_coordinates(location) == (None, None):
                    messages.error(request, f"Invaid location: ${location}")
                else:
                    form.save()
                    messages.success(request, "Event updated successfully!")
                    return redirect("profile")
    else:
        return redirect("events")

    context = {"form": form}
    return render(request, "edit_event_form.html", context)


def deleteEvent(request, event_id):
    event = Ecoevent.objects.get(pk=event_id)
    if request.user == event.organizer:
        if request.method == "POST":
            event.delete()
            messages.success(request, "Event deleted successfully!")
            return redirect("profile")
    else:
        return redirect("events")

    context = {"event": event}
    return render(request, "delete_event.html", context)


def editUser(request, user_id):
    user = User.objects.get(pk=user_id)
    form = UserForm(instance=user)

    if request.method == "POST":
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, "User updated successfully!")
            return redirect("profile")

    context = {"form": form}
    return render(request, "user_form.html", context)


def deleteUser(request, user_id):
    user = User.objects.get(pk=user_id)
    if request.method == "POST":
        user.delete()
        messages.success(request, "User deleted successfully!")
        return redirect("events")
    return render(request, "delete_user.html")
