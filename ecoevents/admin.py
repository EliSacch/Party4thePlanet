from django.contrib import admin
from .models import Ecoevent


@admin.register(Ecoevent)
class EcoeventAdmin(admin.ModelAdmin):
    list_filter = ('location', 'category', 'start_datetime')
    readonly_fields = ('created_on', 'modified_on', 'pk')