from . import views
from django.urls import path


urlpatterns = [
    path("", views.home, name="home"),
    path("events/", views.events, name="events"),
    path("event/<str:event_id>/", views.event, name="event"),
    path("map/", views.map, name="map"),
    path("profile/", views.profile, name="profile"),
    path("create_event/", views.createEvent, name="create_event"),
    path("delete_event/<str:event_id>/", views.deleteEvent, name="delete_event"),
    path("edit_event/<str:event_id>/", views.editEvent, name="edit_event"),
    path("edit_user/<str:user_id>/", views.editUser, name="edit_user"),
    path("delete_user/<str:user_id>/", views.deleteUser, name="delete_user"),
]
