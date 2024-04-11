from django.contrib import admin
from .models import Service, Path

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['id', 'creator', 'content', 'created_at', 'price']
    list_filter = ['created_at']
    search_fields = ['creator__profile__user__username', 'content']

@admin.register(Path)
class PathAdmin(admin.ModelAdmin):
    list_display = ['id', 'service', 'origin', 'destination', 'updated_at', 'price', 'departure_time', 'estimated_arrival_time']
    list_filter = ['updated_at']
    search_fields = ['service__creator__profile__user__username', 'origin', 'destination']
    