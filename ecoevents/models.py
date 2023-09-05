from django.db import models
from django.contrib.auth.models import User


class Ecoevent(models.Model):
    organizer = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='recipes')
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=500, blank=True, null=True)
    category = models.CharField(max_length=200)
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
    location = models.CharField(max_length=200)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title
