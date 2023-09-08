from django.shortcuts import render, redirect
from .models import Ecoevent
from .forms import EcoeventForm, UserForm
from django.contrib import messages
import json  # noqa
from django.core import serializers
from django.http import JsonResponse
from django.contrib.auth.models import User


def home(request):
    return render(request, "index.html", {})


def events(request):
    all_events = Ecoevent.objects.all()
    category = request.GET.get("category")
    if category:
        events = all_events.filter(category=category)
    else:
        events = all_events
    context = {"events": events}

    if request.method == "POST":
        id = int(request.POST.get("id", ""))
        if id is not None:
            get_event = Ecoevent.objects.filter(id=id)
            selected_event = serializers.serialize(
                "json",
                get_event,
            )

        return JsonResponse({"selected_event": selected_event})

    return render(request, "events.html", context)


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
    user = request.user

    if request.method == "POST":
        form = EcoeventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.organizer = user
            event.save()
            form.save()
            messages.success(request, "Event created successfully!")
            return redirect("events")

    context = {"form": form}
    return render(request, "event_form.html", context)


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
