from django.contrib import admin

from core.models import Client, Window, System, Solar


# Register your models here.
@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'session_id')


@admin.register(Window)
class WindowAdmin(admin.ModelAdmin):
    list_display = ('id', 'client', 'x', 'y', 'width', 'height')


@admin.register(System)
class SystemAdmin(admin.ModelAdmin):
    list_display = ('id', 'window')


@admin.register(Solar)
class SolarAdmin(admin.ModelAdmin):
    list_display = ('id', 'system', 'color', 'x', 'y', 'radius')
