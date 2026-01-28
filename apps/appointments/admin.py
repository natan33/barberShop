from django.contrib import admin
from .models import Appointment


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = (
        "client",
        "barber",
        "service",
        "start_time",
        "status",
    )

    list_filter = (
        "status",
        "barber",
        "service",
    )

    search_fields = (
        "client__username",
        "client__email",
    )

    ordering = ("-start_time",)
